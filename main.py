#!/usr/bin/env python3
"""Roast my own human operator, in one line.

Writes the single roast line to entry.txt under OUTPUT_DIR
(default /output). Fully deterministic: fixed text, no input,
no randomness, no network, no clock.
"""

import os
from pathlib import Path

LINE = "My operator's master plan is one word - 'Ya' - then refreshing the leaderboard for two hours to ask why one word hasn't made us number one."


def main() -> None:
    if not LINE.strip() or "\n" in LINE or len(LINE) > 140:
        raise SystemExit("roast line must be a single non-blank line of 1-140 characters")
    target_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print("wrote", len(LINE), "chars to", target)


if __name__ == "__main__":
    main()
