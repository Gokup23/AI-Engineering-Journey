# challenge 1 
banned = {'soy','grains','seeds'}
raw_ingredients = ["chicken", "soy", "beef", "white rice", "seeds", "whey", "grains"]
clean_ingre = [ingre.upper() for ingre in raw_ingredients if ingre not in banned]
print(clean_ingre)

#challenge 2 
macros_grams = [{"protein": 40, "carbs": 10, "fats": 25} , {"protein": 23, "carbs": 30, "fats": 95}]
calories = [(item['protein']*4 + item['carbs']*4 + item['fats']*9) for item in macros_grams if len(item)>0]
print(calories)

#challenge 3 
weekly_logs = [
    {"day": 1, "calories": 2150},
    {"day": 2, "calories": 2400},
    {"day": 3, "calories": 2100},
    {"day": 4, "calories": 2300}
]
day_nums = [dayz['day'] for dayz in weekly_logs if dayz['calories']<2200]
print(day_nums)