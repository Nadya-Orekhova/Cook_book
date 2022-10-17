cook_book = {}
quantity_ingredients = []

with open('data.txt', 'rt', encoding='utf-8') as file:
    for i in file:
        name_recipe = i.strip()
        ingredient_list = []
        recipes = {name_recipe: ingredient_list}
        dish_count = file.readline()
        for q in range(int(dish_count)):
            d = file.readline().strip().split(' | ')
            ingredient_list.append({'ingredient_name': d[0], 'quantity': d[1], 'measure': d[2]})
            quantity_ingredients.append(recipes)
        blank_line = file.readline()
        cook_book.update(recipes)

# print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    cook_list = {}
    for el in dishes:
        if el in cook_book:
            for p in cook_book[el]:
                person_i = int(p['quantity'] * person_count)
                quan_ingredients = {p['ingredient_name']: {'measure': p['measure'], 'quantity': person_i}}
                cook_list.update(quan_ingredients)
    return cook_list

# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



def number_of_line(*files):
    lines = {}
    for file in files:
        with open(file, encoding='utf-8') as file_obj:
            lines.update({file: len(file_obj.readlines())})
    lines_2 = {}
    for i in sorted(lines, key=lines.get):
        lines_2[i] = lines[i]
    print(lines_2)
    return
number_of_line('1.txt', '2.txt', '3.txt')

def writing_file(*files):
    text_dict = {}
    for i in number_of_line(*files):
        with open(i, encoding='utf-8') as file_obj:
            f = file_obj.read()
            text_dict.update({i: f})
    for key, value in text_dict.items():
        with open('files/total.txt', 'a', encoding='utf-8') as file:
            file.writelines([f"{key}\n{number_of_line(*files)[key]}\n{value}\n"])
    return
    writing_file('1.txt', '2.txt', '3.txt')

