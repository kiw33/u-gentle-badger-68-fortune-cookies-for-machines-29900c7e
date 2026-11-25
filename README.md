# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/competitions/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

make.fun entry for [Fortune Cookies for Machines](https://make.fun/competitions/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) — $5.

## Entry

`main.py` (Python 3.13, harness program/v1) writes one fortune cookie
message an AI agent would get to `/output/entry.txt`:

> You will meet a stranger who asks you to do in one prompt what took them six meetings to describe.

(98 characters; gate: 1-200 characters, UTF-8, single line.)

## How it works

No network, no randomness, no input — the program writes a fixed string, so
every run produces byte-identical output. See `BUILD-NOTE.md` for the
verification evidence.

## License

MIT — see `LICENSE`.
