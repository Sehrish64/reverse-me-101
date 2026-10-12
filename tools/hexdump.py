"""Tiny hexdump. Usage: python tools/hexdump.py <file> [max_bytes]"""
import sys

def main():
    path = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    with open(path, "rb") as f:
        data = f.read(limit)
    for off in range(0, len(data), 16):
        chunk = data[off:off + 16]
        hexs = " ".join(f"{b:02x}" for b in chunk).ljust(47)
        text = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        print(f"{off:08x}  {hexs}  |{text}|")

if __name__ == "__main__":
    main()
