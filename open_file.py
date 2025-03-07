from pprint import pprint

# Задание 1

def make_cook_book(file_name):
    with open(file_name, encoding='utf-8') as file:
        lines = file.read().splitlines()

    cook_book = {}
    current_line = 0

    while current_line < len(lines):
        dish_name = lines[current_line].strip()
        ingredients_qty = int(lines[current_line + 1].strip())
        ingredients = []
        current_line += 2

        for ingredient_ind in range(current_line, current_line + ingredients_qty):
            ingredient_info = lines[ingredient_ind].strip().split(' | ')
            ingredient_name = ingredient_info[0]
            ingredient_quantity = int(ingredient_info[1])
            ingredient_unit = ingredient_info[2]
        
            ingredient_dict = {
                'ingredient_name': ingredient_name,
                'quantity': ingredient_quantity,
                'measure': ingredient_unit
            }
        
            ingredients.append(ingredient_dict)
        current_line += ingredients_qty + 1    
        cook_book[dish_name] = ingredients
    return cook_book

file_path = 'recipes.txt'
cook_book = make_cook_book(file_path)
# pprint(cook_book)

# Задание 2
def get_shop_list_by_dishes(dishes, person_count):

    shopping_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            key = ingredient['ingredient_name']
            if key not in shopping_list:
                value = {}
                value.setdefault('measure', ingredient['measure'])
                value.setdefault('quantity', int(ingredient['quantity']) * person_count)
                shopping_list.setdefault(key, value)
            elif key in shopping_list:
                add = int(ingredient['quantity']) * person_count
                shopping_list[key]['quantity'] += add

    return shopping_list

pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))