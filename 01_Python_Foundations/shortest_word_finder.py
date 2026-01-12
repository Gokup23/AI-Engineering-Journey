text = input("Enter a sentence to find the shortest word: ")
words = text.split()

shortest_word = words[0]
min_length = len(shortest_word)

for word in words:
    current_length = len(word)
    if current_length < min_length:
        min_length = current_length
        shortest_word = word

print("--- Analysis Complete ---")
print(f"The shortest word is: '{shortest_word}'")
print(f"The length of the shortest word is: {min_length}")