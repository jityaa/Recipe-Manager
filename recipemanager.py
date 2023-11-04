class Recipe:
    def __init__(self, name, ingredients, instructions, category, cook_time):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.cook_time = cook_time

    def view(self):
        recipe_info = {
            "Name": self.name,
            "Ingredients": self.ingredients,
            "Instructions": self.instructions,
            "Category": self.category,
            "Cook Time (minutes)": self.cook_time
        }
        return recipe_info
    
    def edit(self, new_name, new_ingredients, new_instructions, new_category, new_cook_time):
        self.name = new_name
        self.ingredients = new_ingredients
        self.instructions = new_instructions
        self.category = new_category
        self.cook_time = new_cook_time
        print("Recipe updated.")
