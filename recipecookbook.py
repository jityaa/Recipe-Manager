
class Recipe_Book:
    
    #this list will store all the recipe objects that belong to the recipe book
    recipes = []

    #methods
    def __init__(self):
        print("Book opened")

    #display the menu options for the user to pick from
    def display_menu(self):
        print("1. View all recipes")
        print("2. Add a recipe")
        print("3. Delete a recipe")
        print("4. View a recipe")
        print("5. Search for recipes")
        print("0. Exit")
    
    #receive the user input and return their choice
    def get_user_choice(self):
        try:
            choice = int(input("Enter your choice (0-5): "))
            return choice
        #create error with invalid input
        except ValueError:
            print("Invalid input. Please enter a number.")
            return -1
    
    #main user interface loop
    def user_interface(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            #each choice has logic it runs
            if choice == 0:
                print("Book closing...")
                break
            elif choice == 1:
                print("All recipes:", self.view_all_recipes())
            elif choice == 2:
                #add recipe logic
                self.add_recipe_prompt()
                pass
            elif choice == 3:
                #delete recipe logic
                self.delete_recipe_prompt()
                pass
            elif choice == 4:
                name = input("Enter the name of the recipe: ")
                print(self.view(name))
            elif choice == 5:
                #search logic
                self.search_prompt()
                pass
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
    
    #prompt user to add new recipe
    def add_recipe_prompt(self):
        #get recipe details from the user
        name = input("Enter the name of the recipe: ")
        ingredients = input("Enter the ingredients (comma-separated): ").split(', ')
        instructions = {}
        step_number = 1
        while True:
            step = input(f"Enter instruction for step {step_number} (or enter 'done' to finish): ")
            if step.lower() == 'done':
                break
            instructions[step_number] = step
            step_number += 1
        category = input("Enter the category of the recipe: ")
        cook_time = int(input("Enter the cook time in minutes: "))

        #create a new recipe object and add it to the book
        new_recipe = Recipe(name, ingredients, instructions, category, cook_time)
        self.add_recipe(new_recipe)
        print(f"{name} added to the recipe book.")
    
    def add_recipe(self, recipe_object):
        #add a known recipe object to the recipes attribute
        self.recipes.append(recipe_object)
    
    #ask user what the name of the recipe they want to delete is
    def delete_recipe_prompt(self):
        name_to_delete = input("Enter the name of the recipe you want to delete: ")
        self.delete_recipe(name_to_delete)
    
    #delete a recipe from the recipe book
    def delete_recipe(self, name):
        matching_recipes = [recipe for recipe in self.recipes if recipe.name == name]
        if matching_recipes:
            self.recipes.remove(matching_recipes[0])
            print(f"{name} deleted from recipe book.")
        else:
            print(f"{name} not found in recipe book.")

    #view names of all the recipes
    def view_all_recipes(self):
        """iterates through all recipes that are in the recipes attribute and returns their names."""
        return [recipe.name for recipe in self.recipes]
    
    #view details of specific recipes
    def view(self, name):
        matching_recipes = [recipe.view() for recipe in self.recipes if recipe.name == name]
        return matching_recipes[0] if matching_recipes else f"{name} not found in recipe book."    

    #prompt user for search criteria
    def search_prompt(self):
        print("\n*** Search Recipes ***")
        keyword = input("Enter a keyword to search by name: ")
        category = input("Enter a category to search by category: ")
        ingredients = input("Enter ingredients to search by ingredients (comma-separated): ").split(', ')
        cook_time = input("Enter cook time to search by cook time (or press Enter to skip): ")
        
        search_results = self.search(keyword=keyword, category=category, ingredients=ingredients, cook_time=cook_time)
        
        #perform search and return results
        if search_results:
            print("\nSearch Results:")
            for index, recipe_index in enumerate(search_results, start=6):
                recipe = self.recipes[recipe_index]
                print(f"{index}. {recipe.name}")
        
            selected_index = input("\nEnter the number of the recipe you want to view (0 to cancel): ")
            if selected_index.isdigit():
                selected_index = int(selected_index)
                if 6 <= selected_index <= len(search_results) + 5:
                    recipe_to_view = self.recipes[search_results[selected_index - 6]]
                    print("\nViewing Recipe:")
                    print(recipe_to_view.view())
                elif selected_index != 0:
                    print("Invalid input. Please enter a valid recipe number.")
        else:
            print("No recipes found matching the search criteria.")
    
    #search based on the criteria given
    def search(self, keyword=None, category=None, ingredients=None, cook_time=None):
        matching_indices = [
            index for index, recipe in enumerate(self.recipes) if
            (keyword.lower() in recipe.name.lower() if keyword and keyword.lower() != 'skip' else True) and
            (category.lower() in recipe.category.lower() if category and category.lower() != 'skip' else True) and
            (any(ingredient.lower() in ' '.join(recipe.ingredients).lower() for ingredient in ingredients) if ingredients and 'skip' not in [i.lower() for i in ingredients] else True) and
            (cook_time is None or (cook_time.isdigit() and int(cook_time) >= recipe.cook_time) if cook_time and cook_time.lower() != 'skip' else True)
        ]
        
        return matching_indices


#define a class for recipe
class Recipe:
    
    def __init__(self, name, ingredients, instructions, category, cook_time):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.cook_time = cook_time

    #view details of recipe
    def view(self):
        recipe_info = {
            "Name": self.name,
            "Ingredients": self.ingredients,
            "Instructions": self.instructions,
            "Category": self.category,
            "Cook Time (minutes)": self.cook_time
        }
        return(recipe_info)
    
    #edit the recipe
    def edit(self, new_name, new_ingredients, new_instructions, new_category, new_cook_time):
        self.name = new_name
        self.ingredients = new_ingredients
        self.instructions = new_instructions
        self.category = new_category
        self.cook_time = new_cook_time
        print("Recipe updated.")

#create an instance of the recipe book
Peter_Jity_recipe_book = Recipe_Book()

#create some recipe instances and add them to the recipe book
Recipe1 = Recipe("Chicken over rice", ["chicken breast", "white rice", "salt", "onion", "black pepper", "oil"],
                 {1: "Preheat oil in pan on medium-high heat", 2: "add chopped onion to pan",
                  3: "In bowl, mix chicken breast with oil, salt, and black pepper",
                  4: "Separately bring water to a boil and add rice, simmer until water is absorbed",
                  5: "Add chicken to pan. After 10 minutes flip",
                  6: "After chicken is cooked through, plate with rice"},
                 "Savory entree",
                 25)

Recipe2 = Recipe("Chicken under rice", ["chicken breast", "white rice", "salt", "onion", "black pepper", "oil"],
                 {1: "Preheat oil in pan on medium-high heat", 2: "add chopped onion to pan",
                  3: "In bowl, mix chicken breast with oil, salt, and black pepper",
                  4: "Separately bring water to a boil and add rice, simmer until water is absorbed",
                  5: "Add chicken to pan. After 10 minutes flip",
                  6: "After chicken is cooked through, plate with rice"},
                 "Savory entree",
                 25)

Recipe3 = Recipe("Fried eggs", ["Eggs", "oil", "salt", "black pepper"],
                 {1: "Preheat oil in pan on medium heat", 2: "Crack eggs into pan",
                  3: "After 5 minutes season and serve"},
                 "Savory entree",
                 10)

Recipe4 = Recipe("Cereal", ["cereal", "milk"],
                 {1: "Add desired cereal to bowl", 2: "Add milk"},
                 "Breakfast",
                 5)

Recipe5 = Recipe("Ground turkey stir fry",
                 ["ground turkey", "white rice", "salt", "cumin", "black pepper", "oil", "cayenne pepper", "mushrooms", "shredded carrots"],
                 {1: "Preheat oil in pan on medium-high heat", 2: "add chopped mushrooms and shredded carrots to pan",
                  3: "cook until softened, about 5 minutes, then set aside",
                  4: "Separately bring water to a boil and add rice, simmer until water is absorbed",
                  5: "Add ground turkey to the pan and break up gently",
                  6: "cook for 5 min then flip",
                  7: "simmer until fully cooked and spice to taste with salt, black pepper, cumin, and cayenne pepper",
                  8: "add the mushrooms and carrots back to pan",
                  9: "serve over rice"},
                 "Savory entree",
                 25)
Recipe6 = Recipe("Kale chips",
                 ["kale", "oil", "salt"],
                 {1: "Preheat oven to 300 degrees F", 2: "Cut kale into bite sized pieces",
                  3: "Wash and dry kale thoroughly", 4: "Toss kale with oil and salt",
                  5: "Spread kale on baking sheet and bake until edges are crisp and brown, about 25 minutes",
                  6: "Cool and serve"},
                 "Salty appetizer",
                 30)
Recipe7 = Recipe("Roasted asparagus",
                 ["asparagus", "oil", "salt", "black pepper", "red pepper"],
                 {1: "Preheat oven to 400 degrees F", 2: "trim the ends of the asparagus",
                  3: "Wash and dry asparagus thoroughly", 4: "Toss kale with oil, salt, black pepper, and red pepper",
                  5: "Add asparagus to glass dish and roast, about 15 minutes, flip halfway",
                  6: "Cool and serve"},
                 "Salty appetizer",
                 25)
recipes = [Recipe1, Recipe2, Recipe3, Recipe4, Recipe5, Recipe6, Recipe7]
for recipe in recipes:
    Peter_Jity_recipe_book.add_recipe(recipe)

#test the recipe book functionality
if __name__ == "__main__":
    while True:
        Peter_Jity_recipe_book.user_interface()
        another_action = input("Do you want to perform another action? (yes/no): ").lower()
        if another_action != 'yes':
            break

#TEST CHANGE PETERRR