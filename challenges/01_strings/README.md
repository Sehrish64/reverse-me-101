# Challenge 1: Strings never lie

`vault.bin` is a binary file. Somewhere inside it a developer forgot a flag.

**Goal:** find the flag (format `RE{...}`).

**Tools:** `python tools/strings.py challenges/01_strings/vault.bin`
and `python tools/hexdump.py challenges/01_strings/vault.bin`

**Lesson:** programs leak text. Always run `strings` first.
