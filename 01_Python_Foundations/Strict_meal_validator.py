class Meal:
    def __init__(self,name,protein,carbs,fats,ingredients):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.ingredients = ingredients

    def __str__(self):
            return f"{self.name}: {self.protein}g P | {self.carbs}g C | {self.fats}g F"
    
class DietTracker:
    def __init__(self, username):
        self.username = username
    
    def evaluate_meal(self, meal):
        # RULE A: Banned ingredients
        banned = {'soy', 'grains', 'seeds'}
        meal_ingredients_set = set(meal.ingredients)
        
        # If the intersection (&) of the two sets has anything in it, it fails
        if len(banned & meal_ingredients_set) > 0:
            return False
            
        # RULE B: Macro Separation 
        # Fails if BOTH carbs and fats are significantly high (over 5g)
        if meal.carbs > 5 and meal.fats > 5:
            return False
            
        # If it passes both checks
        return True

        
chicken_rice = Meal("Chicken & Rice", protein=50, carbs=45, fats=2, ingredients=["chicken", "white rice"])
salmon_salad = Meal("Salmon Salad", protein=40, carbs=2, fats=25, ingredients=["salmon", "lettuce", "olive oil", "seeds"])
steak_eggs = Meal("Steak and Eggs", protein=60, carbs=1, fats=30, ingredients=["steak", "eggs", "butter"])

tracker = DietTracker("Vinzeku23")

print(chicken_rice)

print(f"chicken & Rice valid?{tracker.evaluate_meal(chicken_rice)}")
