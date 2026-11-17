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

TEXT CAPTURES (added 2026-11-16)
-------------------------------
Most non-PDF sources are not byte copies of what the URL serves. Ingest prepends a
provenance header, extracts article text from HTML, or bundles companion pages into one
raw file. Their hash can never match the remote, so a hash-only check flagged 12 of them
as drifted on the first full sweep, none of which had changed. A gate that cries wolf on
every run is a gate nobody reads.

So when a text capture's hash differs, it is compared by CONTENT. Both sides are reduced
to one stream of letters and digits: HTML is stripped of tags and page chrome (nav,
header, footer, aside, related-post cards), MDX of imports and JSX, and whitespace and
punctuation are dropped. That makes reflow, our extraction's run-together words, and
entity encoding vanish by construction. The streams are then aligned on shared runs of at
least MIN_BLOCK characters, and every gap between runs is classified:

  * The provenance header ingest prepends is stripped EXACTLY before comparing
    (strip_capture_header), so it never needs a positional allowance.
  * Text that MOVED (found intact elsewhere on the other side; a bundle can hold its
    pages in another order) and page chrome present on the live page outside the content
    container (a sidebar contents menu an older capture kept inline) are noted, not failed.
    Both tests apply only to chunks of 24+ characters: a lone digit or word occurs
    somewhere on almost any page, and "7.2 -> 7.3" must not be excused by a stray "2".
  * Short remote-only text at the very start or end (a contact form, a footer line) is
    noted as edge chrome.
  * Everything else is DRIFT: a changed digit, a deleted word, a removed paragraph at the
    start, middle or end.
  * A page marked `capture: bundle` holds several documents while fetch_url serves one,
    so local-only text before the first and after the last long run is its other
    documents, and is tolerated.

Checked against planted edits on real captures (Next.js HTML against extracted text, a
reordered three-page bundle, a byte-copy README): a changed number, a deleted sentence,
a deleted first or last paragraph, a deleted word and a version bump are all reported,
and an unchanged control is not. The known blind spot is markup alone: removing an
<img> or changing an attribute leaves the text unchanged and is not reported.

A remote that barely overlaps the capture at all (under half of it matches) is not drift.
It means fetch_url serves a different document than local_path holds, such as a YouTube
watch page against a transcript. It is reported as MISMATCH, a configuration problem.

BLOCKED FETCHES (added 2026-11-16)
---------------------------------
Bot defenses answer with 200 or 403 and a challenge page: Cloudflare "Just a moment...",
Vercel Security Checkpoint, the SEC's "undeclared automated tool" notice. Those used to
come out as drift or link rot. They are now detected by HTTP status and page signature,
and reported as BLOCKED. They are not a fact about the document, so they do not fail the
gate. Do not "fix" one by putting personal contact details in the User-Agent; drop the
fetch_url and rely on the archived copy instead.

Exit code is 0 when nothing changed, 1 when drift or link rot is found, 2 on
operational error. BLOCKED and MISMATCH are listed but do not fail the run. Link rot is
reported separately from drift: a publisher that moves a file usually answers the old URL
with 200 and an HTML page, which is a changed hash but not a changed document.

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
import html as htmllib
import subprocess
import sys
import tempfile
import unicodedata

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
    # A filename containing spaces ('raw/Robot Research Direction.pdf') is one
    # path, not several tokens: try the whole value first, then fall back.
    whole = os.path.normpath(os.path.join(ROOT, value.strip().strip("`'\"")))
    if os.path.isfile(whole):
        return whole
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


# --------------------------------------------------------------- text captures

TEXT_EXTS = {".md", ".mdx", ".txt", ".html", ".htm", ".rst", ""}
ANCHOR = 200          # a matching run this long (in stream chars) anchors the alignment
MIN_BLOCK = 12        # shorter "matches" are coincidental letters, not shared text
MIN_OVERLAP = 0.5     # below this share of the remote matching, it is a different document
EDGE_CHROME = 200     # remote-only text this short at the very start/end: page chrome, noted

_HTML_DROP = re.compile(
    r"<(script|style|noscript|template|nav|header|footer|aside)\b[^>]*>.*?</\1\s*>",
    re.S | re.I)
_CODE_DROP = re.compile(r"<(script|style|noscript|template)\b[^>]*>.*?</\1\s*>", re.S | re.I)
# Related-post cards: a heading that is nothing but a link to another page.
# A real tag, parsed by shape: a tag name, then attributes of the form name, name=value,
# name="...", name='...'. Quoted values may span lines (blank lines included, which
# some CMSs emit). A bare "<[^>]+>" would eat prose between "x < y" and a later "->",
# and a truncated "<span class=" left by an old extraction would swallow pages; prose
# fails this shape at its first comma, '#' or '=' run, so neither can happen.
_TAG = re.compile(r"""</?[A-Za-z][\w:-]*"""
                  r"""(?:\s+[A-Za-z_:@][-\w:.@]*"""
                  r"""(?:\s*=\s*(?:"[^"]{0,8000}"|'[^']{0,8000}'|[^\s"'<>`=]{1,400}))?)*"""
                  r"""\s*/?>""")
_LINKED_HEADING = re.compile(r"<h[1-6][^>]*>\s*<a\b[^>]*>.*?</a>\s*</h[1-6]\s*>", re.S | re.I)
# Leaf-ish chrome identified by class: post dates/authors, prev/next links, breadcrumbs.
_CHROME = re.compile(
    r"<(ul|ol|span|a|p|div)\b[^>]*class=\"[^\"]*(?:post-info|post-navigation|breadcrumb|"
    r"share-buttons|related-posts)[^\"]*\"[^>]*>.*?</\1\s*>", re.S | re.I)


_HEADER_LINE = re.compile(r"^(#.*|(Source|Sources|Captured|Fetched|Retrieved|URL)s?\b.*|\s+\S.*)$", re.I)


def strip_capture_header(raw):
    """Remove the provenance header ingest prepends to a capture: the opening run of
    '# ...' / 'Source: ...' / 'Captured: ...' lines up to the first blank line, and only
    if that run actually says where the text came from. HTML-comment headers are removed
    with all other comments. Exact removal, so no position-based tolerance is needed."""
    lines = raw.split("\n")
    k = 0
    while k < len(lines) and lines[k].strip() and _HEADER_LINE.match(lines[k]):
        k += 1
    block = "\n".join(lines[:k]).lower()
    if k and k < 15 and any(w in block for w in ("source", "captured", "fetched", "retrieved")):
        return "\n".join(lines[k:])
    return raw


def looks_html(raw):
    head = raw[:4000].lower()
    return "<html" in head or "<!doctype html" in head or "<body" in head


def capture_text(raw):
    """Reduce a capture or a fetched page to plain text. Applied identically to both
    sides, so anything it strips is stripped symmetrically."""
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    # MDX (docs sites): import/export lines and JSX expressions are code, not content.
    # Detected by content, because the remote copy is saved under local_path's extension.
    if re.search(r"^\s*import\s+\w+\s+from\s+['\"]", raw, flags=re.M):
        raw = re.sub(r"^\s*(import|export)\s.*$", " ", raw, flags=re.M)
        for _ in range(5):  # JSX expressions, innermost first
            # an attribute expression (style={...}) becomes an empty value, so the tag
            # keeps its shape and is stripped as a tag; anything else becomes a space
            raw, n1 = re.subn(r"=\s*\{[^{}]*\}", '=""', raw)
            raw, n2 = re.subn(r"\{[^{}]*\}", " ", raw)
            if not (n1 or n2):
                break
    if looks_html(raw):
        raw = _HTML_DROP.sub(" ", raw)
        raw = _LINKED_HEADING.sub(" ", raw)
        raw = _CHROME.sub(" ", raw)
        # Prefer the tightest content container: <article> sits inside <main> on most
        # docs sites, and <main> there still carries the sidebar table of contents.
        for tag in ("article", "main"):
            m = re.search(rf"<{tag}\b.*?</{tag}\s*>", raw, re.S | re.I)
            if m and len(_TAG.sub("", m.group(0)).strip()) > 1000:
                raw = m.group(0)
                break
    raw = _TAG.sub(" ", raw)
    return htmllib.unescape(raw)


def stream(text):
    """Letters and digits only (plus . % $ so 3.6 and 36 stay distinct), NFKC-folded so
    ligatures (fi) and full-width forms compare equal, lowercased. Whitespace and
    punctuation carry no content, and dropping them makes reflow and run-together words
    from older extractions vanish."""
    t = unicodedata.normalize("NFKC", text).lower()
    return "".join(c for c in t if c.isalnum() or c in ".%$")


def _present(chunk, other):
    """True if `chunk` is (almost) wholly present somewhere in `other`, in runs long
    enough to be shared text. Bundled captures split and reorder pages, so a moved
    section is rarely one contiguous substring of the other side."""
    # Short chunks are never "moved": a lone digit or word occurs somewhere on almost
    # any page, so "7.2 -> 7.3" would be excused because a "2" appears elsewhere.
    if len(chunk) < 2 * MIN_BLOCK:
        return False
    if chunk in other:
        return True
    sm = difflib.SequenceMatcher(None, chunk, other, autojunk=False)
    covered = sum(m.size for m in sm.get_matching_blocks() if m.size >= 2 * MIN_BLOCK)
    return covered / len(chunk) >= 0.9


def compare_text(local, remote, bundle=False):
    """-> dict(kind, overlap, framing, notes, changes). kind is 'same', 'drift' or
    'mismatch'. changes: (local_snippet, remote_snippet) pairs that are substantive.
    notes: tolerated moves and edge chrome, reported but not failing.

    bundle=True (frontmatter `capture: bundle`) means local_path holds several documents
    and fetch_url serves one of them, so local-only text before the first and after the
    last long matching run is the other documents, and is tolerated. Without it, the only
    local-only text tolerated is the provenance header, which is stripped exactly."""
    raw_a = strip_capture_header(open(local, encoding="utf-8", errors="replace").read())
    raw_b = open(remote, encoding="utf-8", errors="replace").read()
    a, b = stream(capture_text(raw_a)), stream(capture_text(raw_b))
    # The whole remote page with only tags removed: chrome that capture_text strips from
    # the remote (a sidebar contents menu, say) but an older capture kept inline.
    # Script, style and template content are excluded even here: frameworks such as
    # Next.js embed a second copy of the whole article in a JSON <script>, and a
    # deleted paragraph would otherwise be "found" there and excused as chrome.
    b_full = stream(htmllib.unescape(_TAG.sub(" ", _CODE_DROP.sub(" ", raw_b))))
    if not b:
        return {"kind": "mismatch", "overlap": 0.0, "framing": 0, "notes": [], "changes": []}
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    # Keep only real shared runs. Character alignment otherwise "matches" single letters
    # scattered through unrelated text, which reads as dozens of one-letter edits.
    blocks = [m for m in sm.get_matching_blocks() if m.size >= MIN_BLOCK]
    overlap = sum(m.size for m in blocks) / len(b)
    if overlap < MIN_OVERLAP:
        return {"kind": "mismatch", "overlap": overlap, "framing": 0, "notes": [], "changes": []}
    anchors = [k for k, m in enumerate(blocks) if m.size >= ANCHOR]
    first, last = (anchors[0], anchors[-1]) if anchors else (len(blocks), -1)
    # Gaps: before block 0, between consecutive blocks, after the last block.
    gaps, pa, pb = [], 0, 0
    for k, m in enumerate(blocks + [difflib.Match(len(a), len(b), 0)]):
        if m.a > pa or m.b > pb:
            gaps.append((k, a[pa:m.a], b[pb:m.b]))
        pa, pb = m.a + m.size, m.b + m.size
    framing, notes, changes = 0, [], []
    for k, was, now in gaps:
        edge = (k <= first or k > last) if bundle else (k == 0 or k == len(blocks))
        if edge:
            if bundle:
                framing += len(was)                  # the bundle's other documents
                was = ""
            if now and len(now) <= EDGE_CHROME:
                notes.append(("edge", now))          # short remote-only chrome: noted
                now = ""
            if not was and not now:
                continue
        # Moved, not changed: a bundled capture can hold its pages in a different order
        # from the live site. Text found intact elsewhere on the other side is a move.
        was_moved = bool(was) and (_present(was, b) or _present(was, b_full))
        now_moved = bool(now) and _present(now, a)
        if (not was or was_moved) and (not now or now_moved):
            notes.append(("moved", was or now))
            continue
        changes.append((was, now))
    return {"kind": "drift" if changes else "same", "overlap": overlap,
            "framing": framing, "notes": notes, "changes": changes}


# -------------------------------------------------------------------- checking

_BLOCK_SIGNATURES = [
    ("Cloudflare challenge", re.compile(r"<title>\s*Just a moment\.\.\.|cf-chl|challenge-platform|"
                                        r"Attention Required! \| Cloudflare", re.I)),
    ("Vercel Security Checkpoint", re.compile(r"Vercel Security Checkpoint", re.I)),
    ("SEC automated-tool block", re.compile(r"Undeclared Automated Tool", re.I)),
    ("Akamai access denied", re.compile(r"<title>\s*Access Denied\s*</title>", re.I)),
]


def blocked_reason(path, status):
    """A bot defense, not a document: return why, or None."""
    with open(path, "rb") as fh:
        head = fh.read(65536).decode("utf-8", "replace")
    for label, rx in _BLOCK_SIGNATURES:
        if rx.search(head):
            return f"{label} (HTTP {status})"
    if status in (401, 403, 429):
        return f"HTTP {status}"
    return None


def fetch(url, dest):
    """-> (ok, err, http_status). No -f: a 403 body is evidence of what blocked us."""
    cmd = ["curl", "-sSL", "--max-time", "300", "-A", UA, "-o", dest,
           "-w", "%{http_code}", url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return False, r.stderr.strip()[:200], 0
    status = int(r.stdout.strip() or 0) if r.stdout.strip().isdigit() else 0
    if not os.path.getsize(dest):
        return False, f"empty response (HTTP {status})", status
    return True, "", status


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
    blocked, mismatched, content_same = [], [], []
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
        ok, err, status = fetch(url, tmp)
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

        why = blocked_reason(keep, status)
        if why:
            print(f"  BLOCKED   {name}: {why} — not checkable from here; archived copy unaffected")
            blocked.append((name, why))
            continue

        if ext.lower() in TEXT_EXTS:
            res = compare_text(local, keep, bundle=fm.get("capture", "").strip().lower() == "bundle")
            if res["kind"] == "mismatch":
                print(f"  MISMATCH  {name}: fetch_url serves a different document than "
                      f"local_path holds ({res['overlap']:.0%} overlap) — fix or drop fetch_url")
                mismatched.append(name)
                continue
            if res["kind"] == "same":
                note = f", {res['framing']} chars of capture framing tolerated" if res["framing"] else ""
                print(f"  ok        {name}  (content unchanged; capture differs from page bytes{note})")
                for kind, txt in res["notes"]:
                    print(f"      note: {kind} {txt[:120]!r}")
                content_same.append(name)
                continue
            print(f"\n  DRIFT     {name}")
            print(f"      recorded {recorded[:16]}")
            print(f"      remote   {digest[:16]}")
            print(f"      saved to {os.path.relpath(keep, ROOT)}")
            print(f"      {len(res['changes'])} substantive change(s) in content "
                  f"(letters/digits only; whitespace and punctuation ignored):")
            for was, now in res["changes"][:args.max_blocks]:
                if was:
                    print(f"      - {was[:240]}")
                if now:
                    print(f"      + {now[:240]}")
            if len(res["changes"]) > args.max_blocks:
                print(f"      ... and {len(res['changes']) - args.max_blocks} more")
            drifted.append((name, digest, res["changes"]))
            continue

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
          f"{len(blocked)} blocked; {len(mismatched)} fetch_url mismatch; "
          f"{len(content_same)} text capture(s) unchanged by content; "
          f"{skipped_pinned} skipped as version-pinned")
    if blocked:
        print("\nBlocked fetches are bot defenses, not document changes. They do not fail the "
              "run. Never add personal contact details to the User-Agent to get past one.")
    if mismatched:
        print("\nA mismatch means fetch_url and local_path describe different documents. "
              "Point fetch_url at what was captured, or drop it.")
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
