#!/usr/bin/env python3
"""Speed Napping — a rejected Olympic sport.

One funny single-line sport the Olympics turned down, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line: athletes race to fall asleep fastest in a stadium of 80,000
screaming fans, and snoring disqualifies you. It reads like a real
broadcast event, the twist lands in the final clause, and every word
earns its place inside the 200-character cap.

Pure standard library, no network, deterministic: the same line on
every run.
"""

import os
import sys

ENTRY = (
    "Speed Napping: athletes race to fall asleep fastest in a stadium "
    "of 80,000 screaming fans; snoring disqualifies you."
)


def main() -> int:
    # Self-check against the published gate: UTF-8 text of 1 to 200
    # characters, not only white space. Refuse to write an invalid entry.
    text = ENTRY.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= 200 or not text.strip():
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
