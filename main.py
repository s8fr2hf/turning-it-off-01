#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny line from a hopeless
tech support agent to a desperate customer.

Writes the line to entry.txt in the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
Pure standard library only. The entry is a single line, 1-199
characters, so it fits the competition's limit exactly.
"""

import os
import sys

LINE = "".join(
    [
        "Turning it off and on again won't fix it, ",
        "but it does give us both thirty seconds ",
        "to pretend somebody's in charge.",
    ]
)


def main() -> int:
    line = LINE.strip()
    if not (1 <= len(line) <= 199):
        print(
            f"error: line must be 1-199 characters, got {len(line)}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)

    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
