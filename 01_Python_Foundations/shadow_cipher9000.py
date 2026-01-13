cipher = {
    "a": "@", "b": "8", "c": "(", "d": "|)", "e": "3", 
    "f": "#", "g": "6", "h": "[-]", "i": "!", "j": "_|",
    "k": "|<", "l": "1", "m": "^^", "n": "/\\", "o": "0",
    "p": "|o", "q": "9", "r": "[2]", "s": "5", "t": "7",
    "u": "(_)", "v": "\/", "w": "\/\/", "x": "><", "y": "`/", "z": "2",
    " ": " / " # Space becomes a slash
}

message = input(f"Enter a secret message to encrypt using Shadow Cipher 9000: ").lower()
secret_code = []

for char in message:
    if char in cipher:
        secret_code.append(cipher[char])
    else:
        secret_code.append(char)  # Non-alphabetic characters remain unchanged

encrypted_result = "".join(secret_code)


print("\n--- ENCRYPTED MESSAGE ---")
print(encrypted_result)
print("-------------------------\n")