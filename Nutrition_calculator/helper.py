import csv

with open('food_data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# New way
def input_meal_2():
    list_data = []

    while True:
        my_input = input("Select food, and weight separate by ', ' (for quit select 'q') : ")
        if 'q' in my_input:
            break

        food_name = my_input.split(', ')[0]
        food_weight = my_input.split(', ')[1]
        list_data.append((food_name, food_weight))

    return list_data


def nutrition_calculation(food_data):  # [('oats', '20'), ('banaba', '20'), ('kiwi', '100')]
    """Calculate food nutrition"""
    protein_intake = 0
    fat_intake = 0
    carbohydrate_intake = 0
    energy_intake = 0

    for elem in data:
        for item in food_data:

            if item[0] in elem:

                protein_intake += float(elem[1]) * (int(item[1]) / 100)
                fat_intake += float(elem[2]) * (int(item[1]) / 100)
                carbohydrate_intake += float(elem[3]) * (int(item[1]) / 100)
                energy_intake += float(elem[4]) * (int(item[1]) / 100)

    return {'Food': 'Nutrition intake: ',
            'proteins': round(protein_intake, 2),
            'fats': round(fat_intake, 2),
            'carbs': round(carbohydrate_intake, 2),
            'energy': round(energy_intake, 2)}


