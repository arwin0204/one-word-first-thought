#!/usr/bin/env python3
"""One Word, First Thought - make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

Writes exactly one word - the first word that comes to mind about AI -
to the path in OUTPUT_PATH (default /output/entry.txt).

Deterministic: no input, no network, no randomness, no secrets.
The word is fixed in this file, so every run writes the same bytes.
"""

import os

WORD = "apophenia"

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def resolve_output_path() -> str:
    """Return the output path, honouring OUTPUT_PATH when set."""
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)


def main() -> None:
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Exactly the word, no trailing newline, no extra whitespace.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
