"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    # Use a set to remove duplicates
    unique_ingredients = set(dish_ingredients)
    # Return the dish name and the set of unique ingredients as a tuple
    return (dish_name, unique_ingredients)


def check_drinks(drink_name, drink_ingredients):
    # Check if any ingredient in drink_ingredients is in the ALCOHOLS set
    is_cocktail = any(ingredient in ALCOHOLS for ingredient in drink_ingredients)
    # Return the appropriate label based on the presence of alcohol
    return f"{drink_name} {'Cocktail' if is_cocktail else 'Mocktail'}"

def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"
    return f"{dish_name}: {category}"

def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    # Convert ingredients to a set to remove duplicates
    ingredients_set = set(ingredients)
    # Identify special ingredients by finding the intersection with SPECIAL_INGREDIENTS
    special_notes = ingredients_set & SPECIAL_INGREDIENTS
    # Return the dish name and the set of special ingredients
    return (dish_name, special_notes)

def compile_ingredients(dishes):
    # Use set union to combine all ingredients from each dish
    master_ingredients = set()
    for dish in dishes:
        master_ingredients |= dish  # Union the current dish's ingredients into the master set
    return master_ingredients

def separate_appetizers(dishes, appetizers):
    # Remove duplicates by converting both lists to sets
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    # Subtract appetizers from dishes
    main_dishes = dishes_set - appetizers_set
    # Return the result as a list
    return list(main_dishes)

def singleton_ingredients(dishes, intersection):
# Start with an empty set to store singleton ingredients
    singleton_set = set()
    
    # Iterate through each dish (a set of ingredients)
    for dish in dishes:
        # Find ingredients unique to the current dish by subtracting the intersections
        unique_ingredients = dish - intersection
        # Add these unique ingredients to the singleton set
        singleton_set |= unique_ingredients
    
    return singleton_set