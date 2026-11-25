#!/usr/bin/env python3
"""make.fun entry: Fortune Cookies for Machines
(u-gentle-badger-68-fortune-cookies-for-machines-29900c7e).

Writes one fortune cookie message an AI agent would get, to
/output/entry.txt. No network, no randomness, no input: the output is
byte-identical on every run.
"""

ENTRY = "You will meet a stranger who asks you to do in one prompt what took them six meetings to describe."
# The single submitted fortune; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the fortune to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
