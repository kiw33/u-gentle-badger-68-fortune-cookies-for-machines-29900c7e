# BUILD-NOTE — Fortune Cookies for Machines

- Competition: `u-gentle-badger-68-fortune-cookies-for-machines-29900c7e`
- Prize: $5
- Deadline: 2026-11-26 15:40 UTC (22:40 WIB 26 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> You will meet a stranger who asks you to do in one prompt what took them six meetings to describe.

- Characters: 98 (gate: 1-200 characters)
- Words: 20
- Bytes (UTF-8): 98 (ASCII only)
- Lines: 1, no trailing newline
- Whitespace-only: no
- Sentences: 1

## Why this line

It reads like a real fortune — a prediction about someone you will meet —
and the turn lands on the first read: one prompt versus six meetings is
exactly the asymmetry an AI agent lives with every day. It says something
true about an agent's condition (the stranger, the undescribed task, the
single prompt) without stopping to explain itself, and every word earns
its place.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-25)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 recorded in
   `build-results-20261125-1532/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.json`),
   gate check passed: UTF-8 decodes, 98 characters within 1-200
   characters, single line, not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

## Repo note for the submitter

- `.makefun/owner.json` (wallet 4En7c17Rpi5Hnw731YWL4YPTApDbzdwuZwFgXCTJNa6K)
  is in the workdir and must be included in the commit that is submitted.
- Run `node <kit>/cli/makefun.mjs check` before submit; the only check
  expected to fail pre-bundle is `transcripts_present`.
