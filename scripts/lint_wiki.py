#!/usr/bin/env python3
"""Wiki lint — structural checks over wiki/, per the conventions in CLAUDE.md.

Usage:
    python3 scripts/lint_wiki.py                    # report only
    python3 scripts/lint_wiki.py --fix-source-counts  # rewrite `sources:` from inbound links

Checks:
  1. Frontmatter present and schema-conformant per page type
  2. Broken internal markdown links
  3. Obsidian [[wikilinks]] (banned — GitHub does not resolve them)
  4. Orphan pages (no inbound links; wiki/notes/ exempt — user-owned)
  5. Index coverage (index.md should catalog every page)
  6. `sources:` count vs. distinct inbound links from sources/ pages.
     NOTE ON THE DEFINITION: `sources:` is treated as *the number of distinct source
     pages that markdown-link to this page*. That is a link-hygiene measure, and a
     LOWER BOUND on real provenance — a source discussing an entity in prose without
     linking it does not count. A page reading `sources: 0` therefore means "no
     ingested source page links here," not "undocumented." Fix the back-link, not
     the number.
  7. One-way citations (entity cites a source that does not cite it back)
  8. Date sanity (updated >= created; nothing in the future)
  9. `_stub_` markers in index.md on pages that have outgrown them

Exit code is 0 always — this reports, it does not gate. Fixing is a human decision
(see CLAUDE.md: "Report findings as a punch list. Don't auto-fix without user direction"),
with the single exception of --fix-source-counts, which is mechanical and derivable.
"""
import argparse
import collections
import datetime
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "wiki")
LINK = re.compile(r"\[[^\]]*\]\((?!https?:|mailto:)([^)\s#]+)(#[^)]*)?\)")
WIKILINK = re.compile(r"(?<!\!)\[\[([^\]]+)\]\]")
FM_LINE = re.compile(r"^([a-zA-Z_]+):\s*(.*)$")
DATE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

# Pages that are catalogs/journals rather than content, exempt from orphan + schema checks.
EXEMPT = {"index.md", "log.md", "overview.md", "backlog.md", "glossary.md"}
STUB_LINE_THRESHOLD = 45  # lines above which a `_stub_` marker looks stale


def load():
    files = sorted(
        os.path.join(d, f)
        for d, _, fs in os.walk(ROOT)
        for f in fs
        if f.endswith(".md")
    )
    return files, {f: open(f, encoding="utf-8").read() for f in files}


def frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    out = {}
    for line in text[3:end].splitlines():
        m = FM_LINE.match(line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def parse_date(s):
    m = DATE.match(s or "")
    return datetime.date(*map(int, m.groups())) if m else None


def targets(path, text):
    """Absolute, normalized link targets from one page."""
    base = os.path.dirname(path)
    return {
        os.path.normpath(os.path.join(base, m.group(1))) for m in LINK.finditer(text)
    }


def kind_of(path):
    return os.path.relpath(path, ROOT).split(os.sep)[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix-source-counts", action="store_true",
                    help="rewrite `sources:` on entity/concept pages from inbound sources/ links")
    args = ap.parse_args()

    files, text = load()
    rel = lambda f: os.path.relpath(f, ROOT)
    out = {f: targets(f, text[f]) for f in files}
    today = datetime.date.today()
    findings = collections.OrderedDict()

    def add(key, items):
        if items:
            findings[key] = items

    # 1 + 8: schema and dates
    schema, dates = [], []
    for f in files:
        if os.path.basename(f) in EXEMPT:
            continue
        d, k = frontmatter(text[f]), kind_of(f)
        if not d:
            schema.append(f"{rel(f)}: no frontmatter")
            continue
        for req in ("title", "type", "tags"):
            if req not in d:
                schema.append(f"{rel(f)}: missing `{req}`")
        if k == "sources":
            for req in ("published", "ingested"):
                if req not in d:
                    schema.append(f"{rel(f)}: source missing `{req}`")
            for forbidden in ("created", "updated", "sources"):
                if forbidden in d:
                    schema.append(f"{rel(f)}: source must not carry `{forbidden}`")
        elif k in ("entities", "concepts", "syntheses"):
            for req in ("created", "updated"):
                if req not in d:
                    schema.append(f"{rel(f)}: missing `{req}`")
            if k in ("entities", "concepts") and "sources" not in d:
                schema.append(f"{rel(f)}: missing `sources` count")
        c, u = parse_date(d.get("created", "")), parse_date(d.get("updated", ""))
        if c and u and u < c:
            dates.append(f"{rel(f)}: updated {u} precedes created {c}")
        for label in ("created", "updated", "ingested"):
            v = parse_date(d.get(label, ""))
            if v and v > today:
                dates.append(f"{rel(f)}: {label} {v} is in the future")
    add("schema violations", schema)
    add("date inconsistencies", dates)

    # 2: broken links
    add("broken internal links", [
        f"{rel(f)} -> {os.path.relpath(t, ROOT)}"
        for f in files for t in sorted(out[f]) if not os.path.exists(t)
    ])

    # 3: wikilinks (ignore inline code and fenced blocks — pages may *document* the ban)
    def strip_code(t):
        t = re.sub(r"```.*?```", "", t, flags=re.S)
        return re.sub(r"`[^`\n]*`", "", t)

    add("Obsidian wikilinks", [
        f"{rel(f)}: [[{m.group(1)[:40]}]]"
        for f in files for m in WIKILINK.finditer(strip_code(text[f]))
    ])

    # 4: orphans
    inbound = collections.Counter()
    for f in files:
        for t in out[f]:
            if t != os.path.normpath(f):
                inbound[t] += 1
    add("orphan pages", [
        rel(f) for f in files
        if inbound[os.path.normpath(f)] == 0
        and not rel(f).startswith("notes" + os.sep)
        and os.path.basename(f) not in EXEMPT
    ])

    # 5: index coverage
    index = os.path.join(ROOT, "index.md")
    indexed = out.get(index, set())
    add("pages not linked from index.md", [
        rel(f) for f in files
        if os.path.normpath(f) not in indexed
        and not rel(f).startswith("notes" + os.sep)
        and os.path.basename(f) != "index.md"
    ])

    # 6 + 7: source counts and one-way citations
    cited_by_sources = collections.defaultdict(set)
    for f in files:
        if kind_of(f) != "sources":
            continue
        for t in out[f]:
            cited_by_sources[t].add(os.path.normpath(f))

    drift, oneway, fixes = [], [], []
    for f in files:
        k = kind_of(f)
        if k not in ("entities", "concepts"):
            continue
        d = frontmatter(text[f])
        actual = len(cited_by_sources[os.path.normpath(f)])
        if "sources" in d:
            try:
                claimed = int(d["sources"])
            except ValueError:
                continue
            if claimed != actual:
                drift.append(f"{rel(f)}: claims {claimed}, inbound {actual}")
                fixes.append((f, claimed, actual))
        for t in sorted(out[f]):
            if kind_of(t) == "sources" and os.path.exists(t):
                if os.path.normpath(f) not in out.get(t, set()):
                    oneway.append(f"{rel(f)} -> {rel(t)} (source does not link back)")
    add("`sources:` count drift", drift)
    add("one-way citations", oneway)

    # 9: stale stub markers
    stale = []
    for line in text.get(index, "").splitlines():
        if "_stub_" not in line:
            continue
        m = LINK.search(line)
        if not m:
            continue
        p = os.path.normpath(os.path.join(ROOT, m.group(1)))
        if os.path.exists(p) and len(text[p].splitlines()) > STUB_LINE_THRESHOLD:
            stale.append(f"{os.path.relpath(p, ROOT)} ({len(text[p].splitlines())} lines)")
    add("stale `_stub_` markers", stale)

    # report
    print(f"wiki lint — {len(files)} pages under {os.path.relpath(ROOT)}/\n")
    if not findings:
        print("  clean.")
    for key, items in findings.items():
        print(f"  [{len(items):>4}] {key}")
        for i in items[:10]:
            print(f"          {i}")
        if len(items) > 10:
            print(f"          ... and {len(items) - 10} more")
        print()

    if args.fix_source_counts and fixes:
        for f, _claimed, actual in fixes:
            s = open(f, encoding="utf-8").read()
            s = re.sub(r"^sources:\s*\d+\s*$", f"sources: {actual}", s, count=1, flags=re.M)
            open(f, "w", encoding="utf-8").write(s)
        print(f"  rewrote `sources:` on {len(fixes)} pages from inbound source links.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
