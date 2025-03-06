# Задача 1
from pprint import pprint
with open('recipes.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
proccessed_lines = []
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

pprint(cook_book)


# Задача 2
def get_shop_list_by_dishes(dishes, person_count):

    shopping_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            key = ingredient['ingredient_name']
            value = {}
            value.setdefault('measure', ingredient['measure'])
            value.setdefault('quantity', int(ingredient['quantity']) * person_count)
            shopping_list.setdefault(key, value)

    return shopping_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))