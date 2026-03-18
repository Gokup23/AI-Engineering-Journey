Daily_calorie = 3000
Strict_mode = True
current_ingredient = 'soy'

if Strict_mode and current_ingredient in {"soy","grains","seeds"}:
    print(f"Alert {current_ingredient} is not allowed during strict_mode")
else:
    print(f"Success:{current_ingredient} added , remaning calories:{Daily_calorie}")
