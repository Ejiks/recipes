def cook_book (file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        line_flag = 0
        ingredient = []
        cook_book = {}
        for lines in f:
            if lines != "":
                line_flag += 1
                if line_flag == 1:
                    dish = lines[:-1]
                elif line_flag == 2:
                    recipe_length = int(lines)
                elif line_flag > 2 and recipe_length != 0:
                    recipe_length -= 1
                    ingredient_line = lines.split("|")
                    ingredient += [{'ingredient_name': ingredient_line[0][:-1], 'quantity': int(ingredient_line[1][1:-1]), 'measure': ingredient_line[2][1:-1]}]
                elif recipe_length == 0:
                    cook_book[dish] = ingredient
                    line_flag = 0
                    ingredient = []
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, file_name):
    menu = cook_book(file_name)
    ingredients = {}
    for dish in dishes:
        for ingridient in menu.get(dish):
            ingredients[ingridient.get('ingredient_name')] = {'quantity': ingridient.get('quantity')*person_count*dishes.count(dish), 'measure': ingridient.get('measure')}
    return ingredients


print(cook_book("recipes.txt"))
print()
print(get_shop_list_by_dishes(["Омлет", "Омлет", "Омлет"], 1, "recipes.txt"))




