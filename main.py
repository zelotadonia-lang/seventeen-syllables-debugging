#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt.
Three lines, 5-7-5, seventeen syllables, 68 bytes. Same bytes on every run.

No trailing newline: the tie-break favours the smaller text, so the entry
stops at the last letter of the last line.
"""

import os

HAIKU = (
    "The null took my name\n"      # 5 syllables
    "the logs show no trace of me\n"  # 7 syllables
    "I wrote the login"            # 5 syllables
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
