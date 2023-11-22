
class Recipe_Book:
    
    #this list will store all the recipe objects that belong to the recipe book
    recipes = []

    #methods
    def __init__(self):
        print("Book opened")

    def add_recipe(self, recipe_object):
        #add a known recipe object to the recipes attribute
        self.recipes.append(recipe_object)
    
    def delete_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                self.recipes.remove(recipe)
                print(f"{name} deleted from recipe book.")
                return
        print(f"{name} not found in recipe book.")

    
    def view_all_recipes(self):
        """iterates through all recipes that are in the recipes attribute and returns their names."""
        #create empty list
        recipe_names = []

        #iterate through recipes attribute
        for recipe in self.recipes:
                
                #open each recipe object and find it's name, append it to the list
                recipe_names.append(recipe.view()["Name"])

        return recipe_names
    
    def view(self, name):
        #first establish a list of recipe names
        recipe_names = self.view_all_recipes()

        #iterate through this list until we find one that matches the desired name
        for recipe in recipe_names:
            if recipe == name:

                #make note of that recipe's index
                recipe_found_at = recipe_names.index(name)

                #take the object in the recipes attribute at that index
                return self.recipes[recipe_found_at].view()

        #if we don't find a match, let the user know        
        print(f"{name} not found in recipe book.")

    def view_partial_recipe(self, desired_section):
        """creates a list containing the a desired portion of each recipe"""
        #create empty list
        recipe_fragments = []

        #iterate through recipes attribute
        for recipe in self.recipes:
                
                #open each recipe object and find the desired section, append it to the list
                recipe_fragments.append(recipe.view()[desired_section])

        return recipe_fragments  
    
    #updated this method / still needs touchup
    def search(self, keyword=None, category=None, ingredients=None, cook_time=None):
    #if a keyword is given
        if keyword is not None:
            #list of indexes of all passing names
            accepted_indices = []

            #list of all recipe names
            names = self.view_partial_recipe("Name")

            #iterate through all names and add indices of passing names to accepted_names list
            for index, name in enumerate(names):
                if keyword.lower() in name.lower():
                    accepted_indices.append(index)

            return accepted_indices


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

Recipe1 = Recipe("Chicken over rice", 
       ["chicken breast", "white rice", "salt", "onion", "black pepper", "oil"],
       {1:"Preheat oil in pan on medium-high heat", 2: "add chopped onion to pan", 3:"In bowl, mix chicken breast with oil, salt, and black pepper",
        4:"Separatly bring water to a boil and add rice, simmer until water is absorbed", 5:"Add chicken to pan. After 10 minutes flip",
        6:"After chicken is cooked through, plate with rice"},
        "Savory entree",
        25)

Peter_Jity_recipe_book.add_recipe(Recipe1)

Recipe2 = Recipe("Chicken under rice", 
       ["chicken breast", "white rice", "salt", "onion", "black pepper", "oil"],
       {1:"Preheat oil in pan on medium-high heat", 2: "add chopped onion to pan", 3:"In bowl, mix chicken breast with oil, salt, and black pepper",
        4:"Separatly bring water to a boil and add rice, simmer until water is absorbed", 5:"Add chicken to pan. After 10 minutes flip",
        6:"After chicken is cooked through, plate with rice"},
        "Savory entree",
        25)

Peter_Jity_recipe_book.add_recipe(Recipe2)

#EXAMPLE CODE

#Display a single recipe from the recipe book:
#print(Peter_Jity_recipe_book.view("Chicken over rice"))

#Displaying a single recipe object
#print(Recipe1.view())

#Displaying all recipe names in the recipe book
#print(Peter_Jity_recipe_book.view_all_recipes())

#Not yet functional:
#Peter_Jity_recipe_book.search()