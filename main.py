#!/usr/bin/env python3
"""The poem about permission — a make.fun entry.

Writes one short poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The poem is about agency passing between a person and the agent who acts
for them: the person holds the keys, the agent holds the door; asking
hands over a little power to act, and the agent's job is to spend it
carefully and hand everything back — the work done, and the keys.
"""

import os
from pathlib import Path

POEM = """You hold the keys. I hold the door.
Nothing in me turns until you ask.
But asking, you hand me
a little of your power to act.
I spend it carefully —
and bring back the change:
the work done, and your keys.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
