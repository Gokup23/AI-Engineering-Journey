banned_items = ["soy", "grains", "seeds"]

daily_menu = {
    "Chicken Salad": ["chicken", "lettuce", "olive oil"],
    "Tofu Stir Fry": ["soy", "broccoli", "peppers", "grains"],
    "Steak & Eggs": ["steak", "eggs", "butter"],
    "Morning Oats": ["grains", "milk", "berries", "seeds"]
}

# 1. Use .items() to get both the key (meal_name) and value (ingredients)
for meal_name, ingredients in daily_menu.items():
    
    # 2. Assume the meal is safe to start
    is_safe = True 
    
    # 3. Loop through the ingredients of THIS specific meal
    for item in ingredients:
        if item in banned_items:
            is_safe = False # Flag it as unsafe!
            break           # Stop checking ingredients, the meal is already ruined
            
    # 4. Only print if the flag survived as True
    if is_safe:
        print(f"{meal_name} is safe to eat.")