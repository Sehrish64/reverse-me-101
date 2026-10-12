"""Like the Unix `strings` tool. Usage: python tools/strings.py <file> [min_len]"""
import re
import sys

def main():
    path = sys.argv[1]
    min_len = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    data = open(path, "rb").read()
    for m in re.finditer(rb"[ -~]{%d,}" % min_len, data):
        print(f"{m.start():08x}: {m.group().decode()}")

if __name__ == "__main__":
    main()
