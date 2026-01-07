# Project: Text Insights Tool
# Topics: Strings, Loops, Control Flow, Booleans

def analyze_text():
    text = input("Enter a sentence to analyze: ").strip()


   # Task A: word count
    simple_word_count = len(text.split())

   # Task B: vowel count
    vowels = "aeiou"
    vowel_count = 0
    for x in text.lower():
      if x in vowels:
        vowel_count += 1
    
  # Task C: Palindrome check
    is_palindrome = text == text[::-1]

  # Task D: Reverse the text
    reversed_text = text[::-1]

    print(f"\n--- Analysis Results ---")
    print(f"Original Text: {text}")
    print(f"Word Count: {simple_word_count}")
    print(f"Vowel Count: {vowel_count}")
    print(f"Is Palindrome: {is_palindrome}")
    print(f"Reversed Text: {reversed_text}")

if __name__ == "__main__":
    analyze_text()

