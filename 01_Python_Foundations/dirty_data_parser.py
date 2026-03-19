raw_scrape = "   PROTEIN: 31.5g | CARBS: 0g | FATS: 3.6g   "

# 1. Aggressively clean the string: remove 'g' and '|'
cleaned_scrape = raw_scrape.replace("g", "").replace("|", "")
# Result: "   PROTEIN: 31.5  CARBS: 0  FATS: 3.6   "

# 2. Split into a list of words
words = cleaned_scrape.split()
# Result: ['PROTEIN:', '31.5', 'CARBS:', '0', 'FATS:', '3.6']

# 3. Extract by index and cast to float
# The numbers are cleanly sitting at odd indexes!
protein = float(words[1])
carbs = float(words[3])
fats = float(words[5])

# 4. Calculate and format
total_calories = (protein * 4) + (carbs * 4) + (fats * 9)
print(f"Total Calories: {total_calories}")