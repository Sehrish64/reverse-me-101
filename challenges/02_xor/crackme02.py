"""Challenge 2. Find the password this program accepts."""
KEY = 0x2A
DATA = [120, 111, 81, 82, 69, 88, 117, 67, 89, 117, 88, 79, 92, 79, 88, 89, 67, 72, 70, 79, 87]

def check(password: str) -> bool:
    return [ord(c) ^ KEY for c in password] == DATA

if __name__ == "__main__":
    pw = input("Password: ")
    print("Access granted!" if check(pw) else "Wrong password.")
