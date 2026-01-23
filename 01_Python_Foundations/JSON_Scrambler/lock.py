import json

def scramble_data():
    with open ('notes.json', 'r') as f:
        data = json.load(f)

        encrypted_data = {}

        print("--- Scrambling Data ---")

        for key,value in data.items():
            # LOGIC: List Comprehension to shift every char by +1
        # ord(c) gets the number, +1 adds to it, chr() turns it back to letter
            cipher_text = "".join([chr(ord(char) + 1) for char in value])

            encrypted_data[key] = cipher_text
        print(f" {value} -> {cipher_text}")

    with open("locked.json",'w' ) as f:
        json.dump(encrypted_data, f , indent=4)

        print("/n Data Scrambled and saved to locked.json")

if __name__ == "__main__":
    scramble_data()