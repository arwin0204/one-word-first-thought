#!/usr/bin/env python3
"""One Word, First Thought - make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word - the first word that comes to mind about AI -
to the path in OUTPUT_PATH (default /output/entry.txt).

Deterministic: no input, no network, no randomness, no secrets.
The word is fixed in this file, so every run writes the same bytes.
"""

import os

WORD = "apophenia"


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Exactly the word, no trailing newline, no extra whitespace.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
