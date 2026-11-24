#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt.
Three lines, 5-7-5, seventeen syllables, 73 bytes. Same bytes on every run.

No trailing newline: the tie-break favours the smaller text, so the entry
stops at the last letter of the last line.

Round 3 revision: tournament winner T3 of 12 candidates, a new concept
after round 2 (rank 444/2958). Prod read the wrong key, the secrets wore
test names, and the demo showed them live.
"""

import os

HAIKU = (
    "Prod read the dev key\n"  # 5 syllables
    "all our secrets wore test names\n"  # 7 syllables
    "we demoed them live"  # 5 syllables
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
