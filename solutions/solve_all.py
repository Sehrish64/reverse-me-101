"""SPOILERS! Run from the repo root: python solutions/solve_all.py"""
import hashlib
import re
import sys
sys.path.insert(0, ".")

# 1
blob = open("challenges/01_strings/vault.bin", "rb").read()
print("1:", re.search(rb"RE\{[^}]*\}", blob).group().decode())

# 2
sys.path.insert(0, "challenges/02_xor")
import crackme02
print("2:", "".join(chr(b ^ crackme02.KEY) for b in crackme02.DATA))

# 3
sys.path.insert(0, "challenges/03_shift")
import crackme03
print("3:", "".join(chr((d - i * 3) % 256) for i, d in enumerate(crackme03.DATA)))

# 4
sys.path.insert(0, "challenges/04_pin")
import crackme04
for n in range(10000):
    pin = f"{n:04d}"
    out = crackme04.unlock(pin)
    if out:
        print("4:", out, "(PIN", pin + ")")
        break

print("5: see challenges/05_network/README.md (curl -H 'X-Auth: <token from proxy>' .../api/v1/secret)")
