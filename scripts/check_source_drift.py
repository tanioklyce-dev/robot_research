#!/usr/bin/env python3
"""Source drift — fingerprint ingested source files and detect silent upstream revision.

Usage:
    python3 scripts/check_source_drift.py --backfill        # write missing sha256: into frontmatter
    python3 scripts/check_source_drift.py --backfill --dry-run
    python3 scripts/check_source_drift.py --check           # re-fetch fetch_url pages, compare, diff
    python3 scripts/check_source_drift.py --check --only ai-index
    python3 scripts/check_source_drift.py --diff OLD.pdf NEW.pdf   # diff two PDFs directly

WHY THIS EXISTS
---------------
Added 2026-08-29 after the Stanford HAI AI Index 2026. That report was ingested
2026-05-09 from an April export. On 2026-06-29 HAI re-exported the PDF and replaced
it *at the same URL*, with no version string in the filename, no changelog, and no
notice in the document. The revision silently corrected a section 2.7 vendor-table
row (Toyota Research Institute, described as a Japanese teleoperated-logistics
company, corrected to a US research lab doing diffusion policy and large behavior
models), restated a figure's provenance from "survey-based estimates" to "Microsoft
telemetry", and moved a headline adoption number by ten points.

Ingest recorded a *date* but not a *fingerprint*, so nothing in the wiki could have
detected any of that. A date says when we looked; only a hash says what we saw.

WHAT DRIFTS, AND WHAT DOESN'T
-----------------------------
Not every source needs re-checking, and pretending otherwise wastes bandwidth on
files that cannot change:

  * arXiv and other versioned artifacts pin their revision in the filename
    (2010.11929v2.pdf). A new version is a new URL and a new file. Drift is
    *visible* by construction, so `--check` skips these unless --include-pinned.
  * Institutional and vendor PDFs — annual reports, datasheets, spec sheets,
    white papers, standards — are the silent-drift class: stable URL, no version,
    re-exported in place. These are what this script is for.

The `sha256:` field is still recorded for *both*, because the fingerprint is worth
having even when the remote is pinned: it detects local corruption, a wrong file
committed under the right name, and Git LFS objects that never got pulled.

GIT LFS
-------
raw/*.pdf is LFS-tracked and this working tree usually has many objects un-pulled
(32 of 187 at the time of writing) — those files are 130-byte text pointers, not
PDFs. Hashing a pointer would record a confident, well-formed, completely wrong
fingerprint. This is the failure this script most had to avoid.

It doesn't need to pull them: an LFS pointer's `oid sha256:` IS the SHA-256 of the
file's real content, by spec. So a pointer is read, not hashed, and the recorded
fingerprint is identical either way. Pull state never changes the answer.

THE NOISE PROBLEM
-----------------
A naive text diff of two PDF exports of the same document is unreadable, and there are
two distinct causes that need two distinct answers.

1. REFLOW AND KERNING. Re-exporting emits different line breaks and kerning-split
   tokens ("United S tates, 26 .30%") on pages a reader would call identical. Answer:
   compare with ALL whitespace removed. Pure whitespace perturbation vanishes; a changed
   word, number, or table cell survives. This took the AI Index comparison from a
   153-line hand diff to its 6 real changes — two of which the hand diff had MISSED,
   both corrected deltas on chart data labels that the eye slides straight past.

2. REPAGINATION. Inserting a subsection mid-document pushes body text onto every later
   page, so comparing page i to page i calls the entire remainder changed. Against the
   Cosmos 3 technical report that reported 81 changed pages for what was one added
   section. Answer: diff the whole document as one token stream and map each change back
   to a page. The insertion is then one insertion, and the rest matches.

What survives both is table-of-contents and cross-reference renumbering, which IS a real
text change but not a content change. Those are counted and reported separately rather
than hidden, and the test for them is deliberately narrow — a lone bare integer moving by
at most 3 — so decimals (91.26 -> 91.36, +2.20 -> +2.10) and larger jumps (54 -> 64) can
never be swallowed by it.

NETWORK
-------
Fetching goes through curl, not urllib, deliberately: several publishers in this
wiki's source list 403 a default Python user-agent (see the docs-site notes in
CLAUDE.md), and curl with a browser UA is what has actually worked here.

Exit code is 0 when nothing changed, 1 when drift or link rot is found, 2 on
operational error. Link rot is reported separately from drift: a publisher that
moves a file usually answers the old URL with 200 and an HTML page, which is a
changed hash but not a changed document.

Unlike lint_wiki.py this one is a gate — drift is a fact about the world, not a style
opinion, so it is safe to fail a scheduled run on it. It still never
edits a wiki page outside --backfill, and --backfill only ever ADDS a missing
sha256; it will not overwrite one that is already there (see --reseal).
"""
import argparse
import datetime
import difflib
import hashlib
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "wiki", "sources")

FM_LINE = re.compile(r"^([a-zA-Z_0-9]+):\s*(.*)$")
LFS_OID = re.compile(r"^oid sha256:([0-9a-f]{64})$", re.M)
# 2010.11929v2.pdf, 1706.03762v7.pdf — an explicit revision in the name
PINNED = re.compile(r"v\d+\.pdf$|/v\d+/")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


# ---------------------------------------------------------------- frontmatter

def split_frontmatter(text):
    """-> (dict, start_index, end_index) or (None, 0, 0). Preserves raw offsets so
    --backfill can splice a line in without reserializing (and reordering) YAML."""
    if not text.startswith("---"):
        return None, 0, 0
    end = text.find("\n---", 3)
    if end < 0:
        return None, 0, 0
    out = {}
    for line in text[3:end].splitlines():
        m = FM_LINE.match(line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out, 3, end


def resolve_local(value):
    """local_path values are mostly clean ('raw/foo.pdf') but 20 read `null` and a
    few carry trailing prose ('raw/x.pdf (preprint); raw/y.pdf'). Take the first
    whitespace-delimited token that resolves to a real file under the repo."""
    if not value or value.lower() in ("null", "none", "-"):
        return None
    for tok in re.split(r"[\s;,]+", value):
        tok = tok.strip("`'\"()")
        if not tok or tok.startswith("http"):
            continue
        p = os.path.normpath(os.path.join(ROOT, tok))
        if os.path.isfile(p):
            return p
    return None


def content_sha256(path):
    """SHA-256 of the file's true content. For an un-pulled Git LFS pointer this is
    read from the pointer's oid rather than computed — same value, no 20 GB pull."""
    with open(path, "rb") as fh:
        head = fh.read(200)
    if head.startswith(b"version https://git-lfs"):
        m = LFS_OID.search(head.decode("utf-8", "replace"))
        if m:
            return m.group(1), "lfs-pointer"
        return None, "lfs-pointer-unparseable"
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest(), "hashed"


def pages():
    for name in sorted(os.listdir(SOURCES)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(SOURCES, name)
        text = open(path, encoding="utf-8").read()
        fm, s, e = split_frontmatter(text)
        if fm is None:
            continue
        yield path, name, text, fm, s, e


# ------------------------------------------------------------------- backfill

def backfill(args):
    written = skipped = unresolved = 0
    pointers = 0
    for path, name, text, fm, s, e in pages():
        local = resolve_local(fm.get("local_path"))
        if local is None:
            if fm.get("local_path") and fm["local_path"].lower() not in ("null", "none"):
                unresolved += 1
                print(f"  unresolved local_path  {name}: {fm['local_path'][:60]}")
            continue
        if "sha256" in fm and not args.reseal:
            skipped += 1
            continue
        digest, how = content_sha256(local)
        if digest is None:
            print(f"  ERROR {name}: {how} for {os.path.relpath(local, ROOT)}")
            continue
        if how == "lfs-pointer":
            pointers += 1

        if args.reseal and "sha256" in fm:
            if fm["sha256"] == digest:
                skipped += 1
                continue
            print(f"  RESEAL {name}: {fm['sha256'][:12]} -> {digest[:12]}")
            new_text = re.sub(r"^sha256:.*$", f"sha256: {digest}", text, count=1, flags=re.M)
        else:
            # Splice directly after local_path so the fingerprint sits with the file
            # it describes, rather than reserializing the block and shuffling keys.
            lines = text[s:e].splitlines(keepends=True)
            for i, line in enumerate(lines):
                if line.startswith("local_path:"):
                    lines.insert(i + 1, f"sha256: {digest}\n")
                    break
            else:
                lines.append(f"sha256: {digest}\n")
            new_text = text[:s] + "".join(lines) + text[e:]

        if not args.dry_run:
            open(path, "w", encoding="utf-8").write(new_text)
        written += 1

    verb = "would write" if args.dry_run else "wrote"
    print(f"\n{verb} {written} sha256 field(s); {skipped} already sealed; "
          f"{unresolved} unresolved local_path")
    if pointers:
        print(f"  ({pointers} read from Git LFS pointers without pulling the object)")
    return 0


# ----------------------------------------------------------------- pdf diffing

def pdf_pages_text(path):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("ERROR: pypdf not installed (pdftotext is broken in this environment)",
              file=sys.stderr)
        raise SystemExit(2)
    reader = PdfReader(path)
    out = []
    for pg in reader.pages:
        try:
            out.append(pg.extract_text() or "")
        except Exception as exc:  # a damaged page should not abort a 425-page diff
            out.append(f"<<EXTRACT_ERROR {exc}>>")
    return out


def denoise(s):
    """Drop ALL whitespace. Re-export reflow and kerning splits are pure whitespace
    perturbation; a real edit is not. This is the whole noise filter."""
    return re.sub(r"\s+", "", s)


def doc_tokens(pages_text):
    """Flatten a document to [(word, page_number)]. Diffing the whole token stream
    rather than page-against-page is what makes reflow survivable: inserting a
    subsection on page 33 pushes body text onto every later page, so a page-indexed
    comparison reports the entire rest of the document as changed. Against the Cosmos 3
    technical report that produced 81 'changed' pages for what was one added section.
    On a token stream the same edit is one insertion and everything after it matches."""
    return [(w, i + 1) for i, page in enumerate(pages_text) for w in page.split()]


def is_renumbering(was, now):
    """True for a lone integer nudged by a page or two — a table-of-contents entry or
    cross-reference shifted by an inserted page. Deliberately narrow: it requires a
    SINGLE bare integer on each side, so decimals (91.26 -> 91.36, +2.20 -> +2.10) and
    larger jumps (54 -> 64) are never swallowed. These are counted and reported, not
    silently dropped."""
    if len(was) != 1 or len(now) != 1:
        return False
    a, b = was[0].rstrip("."), now[0].rstrip(".")
    if not (a.isdigit() and b.isdigit()):
        return False
    return abs(int(a) - int(b)) <= 3


def diff_pdfs(old, new, label_old="old", label_new="new"):
    """-> (substantive, renumbering_count).

    `substantive` is a list of (page, removed_words, added_words), page-ordered."""
    a, b = pdf_pages_text(old), pdf_pages_text(new)
    if len(a) != len(b):
        print(f"      page count differs: {label_old}={len(a)}  {label_new}={len(b)}")
    ta, tb = doc_tokens(a), doc_tokens(b)
    ka = [denoise(w) for w, _ in ta]
    kb = [denoise(w) for w, _ in tb]
    # autojunk would treat any token appearing in >1% of the stream as noise, which on
    # running prose means most function words. Off, or the alignment is meaningless.
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)

    substantive, renumbering = [], 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        was = [w for w, _ in ta[i1:i2]]
        now = [w for w, _ in tb[j1:j2]]
        if denoise(" ".join(was)) == denoise(" ".join(now)):
            continue
        if is_renumbering(was, now):
            renumbering += 1
            continue
        page = ta[i1][1] if i1 < len(ta) else (tb[j1][1] if j1 < len(tb) else 0)
        substantive.append((page, was, now))
    return substantive, renumbering


def render_diff(substantive, renumbering, indent="      ", max_blocks=25, max_words=60):
    out = []
    last_page = None
    for page, was, now in substantive[:max_blocks]:
        if page != last_page:
            out.append(f"{indent}--- page {page} ---")
            last_page = page
        if was:
            out.append(f"{indent}- {' '.join(was)[:max_words * 8]}")
        if now:
            out.append(f"{indent}+ {' '.join(now)[:max_words * 8]}")
    if len(substantive) > max_blocks:
        out.append(f"{indent}... and {len(substantive) - max_blocks} more substantive change(s)")
    if renumbering:
        out.append(f"{indent}({renumbering} page-renumbering change(s) in contents/"
                   f"cross-references, not shown — inserted or removed pages shift them)")
    return out


# -------------------------------------------------------------------- checking

def fetch(url, dest):
    cmd = ["curl", "-sSL", "--max-time", "300", "-A", UA, "-o", dest, url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return False, r.stderr.strip()[:200]
    if not os.path.getsize(dest):
        return False, "empty response"
    return True, ""


def looks_like(path, ext):
    """Cheap magic-byte check. A publisher that moves or pulls a file usually answers
    the old URL with 200 and an HTML page rather than a 404, so a 'changed hash' can
    mean the document was replaced by a navigation page. That is link rot, not a
    revision, and it wants a different response — so the two are never conflated."""
    with open(path, "rb") as fh:
        head = fh.read(5)
    if ext.lower() == ".pdf":
        return head.startswith(b"%PDF")
    return True


def check(args):
    drifted, rotted, checked, skipped_pinned = [], [], 0, 0
    for path, name, text, fm, s, e in pages():
        if args.only and args.only not in name:
            continue
        url = fm.get("fetch_url") or fm.get("pdf_url")
        if not url:
            u = fm.get("url", "")
            if u.endswith(".pdf"):
                url = u
        if not url:
            continue
        local = resolve_local(fm.get("local_path"))
        if not local:
            continue
        recorded = fm.get("sha256")
        if not recorded:
            print(f"  {name}: has fetch_url but no sha256 — run --backfill first")
            continue
        if PINNED.search(local) and not args.include_pinned:
            skipped_pinned += 1
            continue

        checked += 1
        with tempfile.NamedTemporaryFile(suffix=os.path.splitext(local)[1],
                                         delete=False) as tf:
            tmp = tf.name
        ok, err = fetch(url, tmp)
        if not ok:
            print(f"  FETCH FAILED {name}: {err}")
            os.unlink(tmp)
            continue
        digest, _ = content_sha256(tmp)
        if digest == recorded:
            print(f"  ok        {name}")
            os.unlink(tmp)
            continue

        # Changed. Keep the file — it is evidence, and re-downloading is expensive.
        ext = os.path.splitext(local)[1]
        keep = os.path.join(args.save_dir, f"{name[:-3]}.remote{ext}")
        os.makedirs(args.save_dir, exist_ok=True)
        os.replace(tmp, keep)

        if not looks_like(keep, ext):
            print(f"\n  LINK ROT  {name}")
            print(f"      {url}")
            print(f"      no longer returns {ext} — got {os.path.getsize(keep)} bytes of "
                  f"something else (usually a nav or error page served with 200)")
            print(f"      saved to {os.path.relpath(keep, ROOT)}")
            print("      the archived copy in raw/ is unaffected; update the URL on the page")
            rotted.append((name, url))
            continue

        print(f"\n  DRIFT     {name}")
        print(f"      recorded {recorded[:16]}")
        print(f"      remote   {digest[:16]}")
        print(f"      saved to {os.path.relpath(keep, ROOT)}")
        detail = []
        if ext == ".pdf":
            try:
                detail, renum = diff_pdfs(local, keep)
            except Exception as exc:
                # One unreadable PDF must never abort a sweep of hundreds.
                print(f"      could not diff: {type(exc).__name__}: {exc}")
                detail = []
            else:
                if not detail:
                    print("      no substantive text change — re-export, asset, or "
                          "pagination change only"
                          + (f" ({renum} renumbering)" if renum else ""))
                for line in render_diff(detail, renum, max_blocks=args.max_blocks):
                    print(line)
        drifted.append((name, digest, detail))

    print(f"\nchecked {checked}; {len(drifted)} drifted; {len(rotted)} link-rotted; "
          f"{skipped_pinned} skipped as version-pinned")
    if drifted:
        print("\nDrift is not automatically applied. Review the diff, then update the "
              "source page, re-seal with --backfill --reseal, and log it.")
    if rotted:
        print("\nLink rot does not change what the wiki knows — raw/ still holds the "
              "archived copy. Find the file's new home and update url/fetch_url.")
    return 1 if (drifted or rotted) else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--backfill", action="store_true",
                    help="write a missing sha256: into source-page frontmatter")
    ap.add_argument("--reseal", action="store_true",
                    help="with --backfill, also UPDATE an existing sha256 that no longer "
                         "matches the local file (use after deliberately accepting a revision)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check", action="store_true",
                    help="re-fetch sources that declare fetch_url/pdf_url and compare")
    ap.add_argument("--only", metavar="SUBSTR", help="restrict --check to matching filenames")
    ap.add_argument("--include-pinned", action="store_true",
                    help="also check version-pinned artifacts (arXiv vN etc.)")
    ap.add_argument("--diff", nargs=2, metavar=("OLD", "NEW"),
                    help="diff two PDFs directly, no wiki involved")
    ap.add_argument("--save-dir", default=os.path.join(ROOT, ".drift"),
                    help="where drifted downloads are kept (default: .drift/)")
    ap.add_argument("--max-blocks", type=int, default=25,
                    help="max substantive change blocks to print per source")
    args = ap.parse_args()

    if args.diff:
        changes, renum = diff_pdfs(args.diff[0], args.diff[1])
        if not changes:
            print("no substantive text change (whitespace/reflow only)"
                  + (f"; {renum} page-renumbering change(s)" if renum else ""))
            return 0
        for line in render_diff(changes, renum, indent="", max_blocks=args.max_blocks):
            print(line)
        print(f"\n{len(changes)} substantive change(s)")
        return 1
    if args.backfill:
        return backfill(args)
    if args.check:
        return check(args)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
