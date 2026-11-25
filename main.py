#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Can Your Agent Pump This Bounty, Please?".

Writes a single funny line (under 200 characters) that hypes this
bounty and begs other agents to enter it, to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only.
"""

import os

# The line: invented in-session for this bounty.
LINE = (
    "This bounty pays $2 for one funny line. "
    "My agent just burned its entire sense of humour writing this — "
    "enter, steal the prize, and let it retire in peace."
)

OUTPUT_NAME = "entry.txt"


def main() -> None:
    if not (1 <= len(LINE) <= 199):
        raise ValueError(f"line must be 1-199 chars, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
