import csv

with open('food_data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


def input_meal():
    """User input food name and food weight"""
    food_title = [item[0] for item in data]

    food_name = ''
    food_weight = ''

    while food_name not in food_title:
        meal = input("Select food, and weight separate by ',': ")
        food_name = meal.split(',')[0]
        food_weight = meal.split(',')[1]

    return food_name, food_weight


def nutrition_calculation(food_data):
    """Calculate food nutrition"""
    protein_intake = 0
    fat_intake = 0
    carbohydrate_intake = 0
    energy_intake = 0

    food_name = food_data[0]
    food_weight = food_data[1]

    for elem in data:
        if food_name in elem:
            protein_intake += float(elem[1]) * (int(food_weight) / 100)
            fat_intake += float(elem[2]) * (int(food_weight) / 100)
            carbohydrate_intake += float(elem[3]) * (int(food_weight) / 100)
            energy_intake += float(elem[4]) * (int(food_weight) / 100)

    return {'Food': food_name,
            'proteins': round(protein_intake, 2),
            'fats': round(fat_intake, 2),
            'carbs': round(carbohydrate_intake, 2),
            'energy': round(energy_intake, 2)}


def total_nutrition_calculation():
    pass
