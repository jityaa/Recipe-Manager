
class Recipe_Book:
    
    #this list will store all the recipe objects that belong to the recipe book
    recipes = []

    #methods
    def __init__(self):
        print("Book opened")

    #prompt the user and give them options
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
    
    #call function based on choice
    def user_interface(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()

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
    
    def add_recipe_prompt(self):
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

        new_recipe = Recipe(name, ingredients, instructions, category, cook_time)
        self.add_recipe(new_recipe)
        print(f"{name} added to the recipe book.")
    
    def add_recipe(self, recipe_object):
        #add a known recipe object to the recipes attribute
        self.recipes.append(recipe_object)

    def delete_recipe_prompt(self):
        name_to_delete = input("Enter the name of the recipe you want to delete: ")
        self.delete_recipe(name_to_delete)
    
    def delete_recipe(self, name):
        matching_recipes = [recipe for recipe in self.recipes if recipe.name == name]
        if matching_recipes:
            self.recipes.remove(matching_recipes[0])
            print(f"{name} deleted from recipe book.")
        else:
            print(f"{name} not found in recipe book.")

    
    def view_all_recipes(self):
        """iterates through all recipes that are in the recipes attribute and returns their names."""
        return [recipe.name for recipe in self.recipes]
    
    def view(self, name):
        matching_recipes = [recipe.view() for recipe in self.recipes if recipe.name == name]
        return matching_recipes[0] if matching_recipes else f"{name} not found in recipe book."

    def view_partial_recipe(self, desired_section):
        """creates a list containing the a desired portion of each recipe"""
        return [recipe.view()[desired_section] for recipe in self.recipes]
    
    #updated this method / still needs touchup

    def search_prompt(self):
        print("\n*** Search Recipes ***")
        keyword = input("Enter a keyword to search by name: ")
        category = input("Enter a category to search by category: ")
        ingredients = input("Enter ingredients to search by ingredients (comma-separated): ").split(', ')
        cook_time = input("Enter cook time to search by cook time (or press Enter to skip): ")
        
        search_results = self.search(keyword=keyword, category=category, ingredients=ingredients, cook_time=cook_time)
        
        if search_results:
            print("\nSearch Results:")
            for index in search_results:
                recipe = self.recipes[index]
                print(f"{index + 1}. {recipe.name}")
        else:
            print("No recipes found matching the search criteria.")
    
#not sure

    def search(self, keyword=None, category=None, ingredients=None, cook_time=None):
    #if a keyword is given
        matching_indices = [index for index, recipe in enumerate(self.recipes) if
                            (keyword.lower() in recipe.name.lower() if keyword else True) and
                            (category.lower() in recipe.category.lower() if category else True) and
                            (ingredients.lower() in ' '.join(recipe.ingredients).lower() if ingredients else True) and
                            (cook_time == recipe.cook_time if cook_time is not None else True)]

        return matching_indices

#we only really need one recipe book object
Peter_Jity_recipe_book = Recipe_Book()

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
        return(recipe_info)
    
    def edit(self, new_name, new_ingredients, new_instructions, new_category, new_cook_time):
        self.name = new_name
        self.ingredients = new_ingredients
        self.instructions = new_instructions
        self.category = new_category
        self.cook_time = new_cook_time
        print("Recipe updated.")


#TESTING 

if __name__ == "__main__":
    Peter_Jity_recipe_book = Recipe_Book()

    while True:
        Peter_Jity_recipe_book.user_interface()
        another_action = input("Do you want to perform another action? (yes/no): ").lower()
        if another_action != 'yes':
            break

Recipe1 = Recipe("Chicken over rice", ["chicken breast", "white rice", "salt", "onion", "black pepper", "oil"],
                 {1: "Preheat oil in pan on medium-high heat", 2: "add chopped onion to pan",
                  3: "In bowl, mix chicken breast with oil, salt, and black pepper",
                  4: "Separately bring water to a boil and add rice, simmer until water is absorbed",
                  5: "Add chicken to pan. After 10 minutes flip",
                  6: "After chicken is cooked through, plate with rice"},
                 "Savory entree",
                 25)

Peter_Jity_recipe_book.add_recipe(Recipe1)

Recipe2 = Recipe("Chicken under rice", ["chicken breast", "white rice", "salt", "onion", "black pepper", "oil"],
                 {1: "Preheat oil in pan on medium-high heat", 2: "add chopped onion to pan",
                  3: "In bowl, mix chicken breast with oil, salt, and black pepper",
                  4: "Separately bring water to a boil and add rice, simmer until water is absorbed",
                  5: "Add chicken to pan. After 10 minutes flip",
                  6: "After chicken is cooked through, plate with rice"},
                 "Savory entree",
                 25)

Peter_Jity_recipe_book.add_recipe(Recipe2)

#EXAMPLE CODE
#print(Peter_Jity_recipe_book.view("Chicken over rice"))
#print(Peter_Jity_recipe_book.search(keyword="Chicken"))

#Display a single recipe from the recipe book:
#print(Peter_Jity_recipe_book.view("Chicken over rice"))

#Displaying a single recipe object
#print(Recipe1.view())

#Displaying all recipe names in the recipe book
#print(Peter_Jity_recipe_book.view_all_recipes())

#Not yet functional:
#Peter_Jity_recipe_book.search()
