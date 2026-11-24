#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one two-sentence horror story to /output/entry.txt.
Standard library only.
"""

import os

STORY = (
    "My new neighbours leave their porch light on all night, and so do I, "
    "so they know someone is looking out for them. "
    "Yesterday they asked me, very politely, to stop standing at the foot of their bed at three in the morning."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
