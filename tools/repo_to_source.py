#!/usr/bin/env python3
"""Turn a public GitHub tree into one NotebookLM-sized markdown plate.

Does not call NotebookLM. Writes a file whose raw URL can be pasted as a web source.
Skips binaries, lockfiles, and anything under return/.
Stops before 500_000 words.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

WORD_CAP = 500_000
SKIP_SUFFIX = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip",
    ".woff", ".woff2", ".ico", ".mp3", ".mp4", ".wav",
}
SKIP_NAMES = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml"}


def words(text: str) -> int:
    return len(text.split())


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("root", type=pathlib.Path)
    p.add_argument("-o", "--out", type=pathlib.Path, default=pathlib.Path("sources/REPO.md"))
    args = p.parse_args()
    root = args.root.resolve()
    parts = [f"# Repo plate\n\nRoot: `{root.name}`\n\n"]
    used = words(parts[0])
    skipped = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith("return/") or path.name in SKIP_NAMES or path.suffix.lower() in SKIP_SUFFIX:
            skipped.append(rel)
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            skipped.append(rel)
            continue
        block = f"\n\n## {rel}\n\n```\n{text.rstrip()}\n```\n"
        n = words(block)
        if used + n > WORD_CAP:
            skipped.append(rel + " (over word cap)")
            break
        parts.append(block)
        used += n
    parts.append("\n\n## Skipped\n\n" + "\n".join(f"- {s}" for s in skipped) + "\n")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {args.out} words={used} skipped={len(skipped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
