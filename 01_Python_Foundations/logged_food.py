logged_food = "Glazed Soy Chunks"
# Convert the split list directly into a Set
ingredients = set(logged_food.lower().split())

strict_diet = True
is_cutting = True

# Use the '&' operator to find any overlaps between the two sets
if strict_diet and (ingredients & {'soy', 'grains', 'seeds'}):
    print('Not allowed during strict diet')
elif is_cutting and (ingredients & {'sugar', 'syrup'}):
    print('Not allowed during cutting phase')
else:
    print('Allowed to eat')