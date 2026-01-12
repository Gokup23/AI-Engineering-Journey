text = input("Enter a sentence to find the longest word: ")
words = text.split()

longest_word = ""
max_length = 0

for word in words:
    current_length = len(word)
    if current_length > max_length:
        max_length = current_length
        longest_word = word


print("--- Analysis Complete ---")
print(f"The longest word is: '{longest_word}'")
print(f"The length of the longest word is: {max_length}")