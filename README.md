# reverse-me-101

Learn reverse engineering by doing. Five small hands-on challenges, zero dependencies,
Python 3.8+ only. Safe, local and legal: everything runs on your own machine.

| # | Challenge | Skill |
|---|-----------|-------|
| 1 | Strings never lie | `strings`, hexdump |
| 2 | XOR | reading code, reversing XOR |
| 3 | Shift by index | writing an inverse function |
| 4 | PIN | hash brute force |
| 5 | Watch the wire | sniffing API traffic |

## Quick start

```bash
git clone https://github.com/<you>/reverse-me-101
cd reverse-me-101
python tools/strings.py challenges/01_strings/vault.bin
```

Each challenge folder has its own README. Flags look like `RE{...}`.
Stuck? Spoilers are in `solutions/` (try first, peek later).

## Tools included

- `tools/hexdump.py` view raw bytes
- `tools/strings.py` extract readable text from any file
- `tools/sniff_proxy.py` local HTTP logging proxy

## Roman Urdu mein

Yeh repo reverse engineering seekhne ke liye hai. Har challenge mein ek chhupa hua
flag (`RE{...}`) dhoondna hai. Pehle `strings` chalayein, phir code parhein, phir
network dekhein. Sab kuch aapke apne computer par chalta hai, kisi aur ki app ya
server par kuch nahi.

## Ethics

Reverse engineer only software and services you own or have written permission to test.
Do not use these techniques for piracy, fraud or unauthorized access.

## Ideas to extend

- Add a challenge with a compiled C binary (use `gdb` / Ghidra)
- Add an Android APK challenge
- Send your own challenge as a pull request

License: MIT
