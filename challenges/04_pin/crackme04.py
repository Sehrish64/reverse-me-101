"""Challenge 4. A 4-digit PIN protects the flag. Only its hash is stored."""
import hashlib

PIN_HASH = "e25f201f9014599e00073db598a2603a9c05766965336d9b9c68c3d4081ee9a3"
FLAG_XOR = [85, 70, 114, 99, 117, 118, 125, 100, 88, 101, 102, 115, 100, 102, 86, 118, 110, 109, 122, 124]

def unlock(pin: str):
    if hashlib.sha256(pin.encode()).hexdigest() != PIN_HASH:
        return None
    return "".join(chr(b ^ int(pin[i % 4])) for i, b in enumerate(FLAG_XOR))

if __name__ == "__main__":
    p = input("PIN: ")
    out = unlock(p)
    print(out if out else "Wrong PIN.")
