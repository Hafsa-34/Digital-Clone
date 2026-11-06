"""Phase 2: load -> clean -> chunk (200-300 words, overlapping) -> metadata.

Usage:
    python src/Chunking.py                  # process data/, print a quality report
    python src/Chunking.py --allow-dummy    # same, but tolerate DUMMY DATA markers (testing only)
    python src/Chunking.py --show 3         # also print the first 3 chunks in full
BuildIndex.py imports load_documents() and build_chunks() from here.
"""
import argparse, glob, math, os, re, statistics, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent      # Digital-Clone/ (works from any working directory)

MIN_WORDS, MAX_WORDS, OVERLAP = 200, 300, 40      # chunk size window and overlap (words)
MIN_TAIL = 60                                      # a final chunk with fewer NEW words is merged back
PLACEHOLDERS = ("[ANSWER]", "TODO", "DUMMY DATA")
ABBREV = ("e.g.", "i.e.", "dr.", "mr.", "mrs.", "ms.", "vs.", "etc.", "approx.", "no.", "fig.")
EXTS = {".md", ".txt", ".pdf"}

# ---------------------------------------------------------------- 1. LOAD
def read_file(path):
    if path.lower().endswith(".pdf"):
        from pypdf import PdfReader                      # pip install pypdf (build time only)
        return "\n".join((p.extract_text() or "") for p in PdfReader(path).pages)
    with open(path, encoding="utf-8-sig") as f:
        return f.read()

def load_documents(data_dir=ROOT / "data", check_placeholders=True):
    docs = []
    for path in sorted(glob.glob(os.path.join(str(data_dir), "*"))):
        ext = os.path.splitext(path)[1].lower()
        if ext not in EXTS:
            continue
        raw = read_file(path)                            # placeholder check runs on RAW text,
        if check_placeholders:                           # before cleaning removes any comments
            for p in PLACEHOLDERS:
                if p in raw:
                    raise ValueError(f"{os.path.basename(path)} still contains '{p}'. "
                                     "Edit it with your real details and delete the marker.")
        docs.append({"source": os.path.basename(path), "kind": ext[1:], "raw": raw})
    if not docs:
        raise FileNotFoundError(f"No .md/.txt/.pdf files in {data_dir}/")
    return docs

# ---------------------------------------------------------------- 2. CLEAN
QUOTES = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", "\u00a0": " "})

def normalize(text, kind="md"):
    text = unicodedata.normalize("NFKC", text).translate(QUOTES)   # ligatures, quotes, dashes
    text = text.replace("\u00ad", "").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)             # HTML comments
    text = re.sub(r"[ \t]+", " ", text)
    if kind == "pdf":                                              # undo hard line wraps + hyphenation
        text = re.sub(r"-\n(?=[a-z])", "", text)
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    return text

def strip_markup(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)                     # images
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)                 # [text](url) -> text
    s = re.sub(r"\*\*|__|\*|`", "", s)                             # bold / italic / code marks
    return re.sub(r"\s+", " ", s).strip()

# ---------------------------------------------------------------- 3. SENTENCES + STRUCTURE
def split_sentences(line, max_words=MAX_WORDS):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z"(\[])', line)
    merged = []
    for p in parts:                                                # re-join splits after abbreviations
        if merged and merged[-1].lower().endswith(ABBREV):
            merged[-1] += " " + p
        else:
            merged.append(p)
    out = []
    for s in merged:                                               # safety: break absurdly long sentences
        w = s.split()
        for i in range(0, len(w), max_words):
            out.append(" ".join(w[i:i + max_words]))
    return [s for s in out if s.strip()]

def to_units(text):
    """Return (title, [{'text','section'}...]); each unit is one sentence, heading or bullet."""
    title, heading, units = None, "", []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            h = strip_markup(m.group(2)).strip()
            if not h:
                continue
            if len(m.group(1)) == 1 and title is None:
                title = h
            heading = h.rstrip(":")
            units.append({"text": h if h[-1] in ".:?!" else h + ".", "section": heading})
            continue
        line = strip_markup(re.sub(r"^([-*•]|\d+[.)])\s+", "", line))
        for s in split_sentences(line):
            units.append({"text": s, "section": heading or title or ""})
    return title, units

# ---------------------------------------------------------------- 4. CHUNK
def chunk_spans(wc):
    """wc = words per unit. Returns [(start, end, new_start)] spans of unit indices.
    Sizes are balanced per document so chunks land near the 200-300 window, never cut
    mid-sentence, and each chunk after the first starts with ~OVERLAP words of the previous one."""
    total = sum(wc)
    if total <= MAX_WORDS:
        return [(0, len(wc), 0)]
    n = math.ceil((total - OVERLAP) / (MAX_WORDS - OVERLAP))
    target = max((total + (n - 1) * OVERLAP) / n, MIN_WORDS)
    spans, start = [], 0
    while start < len(wc):
        end, w = start, 0
        while end < len(wc) and w < target and (w + wc[end] <= MAX_WORDS or end == start):
            w += wc[end]
            end += 1
        spans.append([start, end, spans[-1][1] if spans else 0])
        if end >= len(wc):
            break
        back, ow = end, 0
        while back - 1 > start and ow < OVERLAP:                   # step back to build the overlap
            back -= 1
            ow += wc[back]
        start = max(back, start + 1)
    if len(spans) > 1:                                             # merge a stub tail into the previous chunk
        s, e, ns = spans[-1]
        ps, pe, _ = spans[-2]
        if sum(wc[ns:e]) < MIN_TAIL and sum(wc[ps:e]) <= MAX_WORDS + 40:
            spans[-2][1] = e
            spans.pop()
    return [tuple(s) for s in spans]

def make_chunks(doc):
    title, units = to_units(normalize(doc["raw"], doc["kind"]))
    wc = [len(u["text"].split()) for u in units]
    stem = os.path.splitext(doc["source"])[0]
    spans = chunk_spans(wc)
    chunks = []
    for k, (a, b, ns) in enumerate(spans):
        text = " ".join(u["text"] for u in units[a:b])
        chunks.append({
            "chunk_id": f"{stem}::{k:03d}",
            "source": doc["source"],
            "title": title or stem,
            "section": units[ns]["section"],
            "chunk_index": k,
            "n_chunks": len(spans),
            "word_count": len(text.split()),
            "overlap_words": sum(wc[a:ns]),
            "text": text,
        })
    return chunks

def build_chunks(docs):
    return [c for d in docs for c in make_chunks(d)]

# ---------------------------------------------------------------- 5. VALIDATE / REPORT
def report(chunks, show=0):
    print(f"{'source':38} {'chunks':>6} {'min':>5} {'avg':>5} {'max':>5} {'overlap':>8}")
    problems = []
    by_src = {}
    for c in chunks:
        by_src.setdefault(c["source"], []).append(c)
    for src, cs in by_src.items():
        w = [c["word_count"] for c in cs]
        ov = [c["overlap_words"] for c in cs[1:]]
        print(f"{src:38} {len(cs):>6} {min(w):>5} {int(statistics.mean(w)):>5} {max(w):>5} "
              f"{(str(int(statistics.mean(ov)))+'w') if ov else '-':>8}")
        if max(w) > MAX_WORDS + 40:
            problems.append(f"{src}: a chunk has {max(w)} words (> {MAX_WORDS + 40})")
        for c in cs[1:]:
            if c["overlap_words"] == 0:
                problems.append(f"{c['chunk_id']}: no overlap with previous chunk")
    ids = [c["chunk_id"] for c in chunks]
    if len(ids) != len(set(ids)):
        problems.append("duplicate chunk_ids")
    for c in chunks:
        if not c["text"].strip() or not c["source"] or not c["chunk_id"]:
            problems.append(f"{c['chunk_id']}: empty text or missing metadata")
    allw = [c["word_count"] for c in chunks]
    inwin = sum(MIN_WORDS - 20 <= x <= MAX_WORDS + 20 for x in allw)
    print(f"\n{len(by_src)} documents -> {len(chunks)} chunks | words/chunk min {min(allw)}, "
          f"avg {int(statistics.mean(allw))}, max {max(allw)} | "
          f"{inwin}/{len(chunks)} within ~200-300 (+/-20)")
    print("PROBLEMS:" if problems else "No structural problems found.")
    for p in problems:
        print("  -", p)
    for c in chunks[:show]:
        print(f"\n--- {c['chunk_id']} | section: {c['section']} | {c['word_count']}w | "
              f"overlap {c['overlap_words']}w\n{c['text']}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(ROOT / "data"))
    ap.add_argument("--allow-dummy", action="store_true", help="skip placeholder check (testing only)")
    ap.add_argument("--show", type=int, default=0)
    a = ap.parse_args()
    report(build_chunks(load_documents(a.data, check_placeholders=not a.allow_dummy)), a.show)