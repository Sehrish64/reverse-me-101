"""Challenge 3. The check changes character by character."""
DATA = [82, 72, 129, 114, 122, 115, 119, 141, 119, 136, 127, 149, 152, 140, 156, 160, 173]

def check(password: str) -> bool:
    if len(password) != len(DATA):
        return False
    for i, c in enumerate(password):
        if (ord(c) + i * 3) % 256 != DATA[i]:
            return False
    return True

if __name__ == "__main__":
    pw = input("Password: ")
    print("Access granted!" if check(pw) else "Wrong password.")
