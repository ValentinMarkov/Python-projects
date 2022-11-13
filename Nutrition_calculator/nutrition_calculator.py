import csv
import datetime

with open('food_data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

protein_intake = 0
fat_intake = 0
carbohydrate_intake = 0
energy_intake = 0
food_intake = {}

food_list = []


while True:
    meal = input("What you eat ? ")
    if meal == 'q':
        with open('meals_diary.txt', 'a') as f:
            f.write(
                f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * *"
                f"\nMeal take on: {(datetime.datetime.now())}"
                f"\nThis meal you consume: {food_intake}"
                f"\nTotal nutrition intake:\n\tProtein: {round(protein_intake, 2)} grams"
                f"\n\tFat: {round(fat_intake, 2)} grams"
                f"\n\tCarbohydrate: {round(carbohydrate_intake, 2)} grams"
                f"\n\tEnergy: {round(energy_intake, 2)} cal")
            f.close()
        break

    # Check food name present in database
    food_list = []
    for food in data:
        food_list.append(food[0])

    if meal not in food_list:
        print('We don\'t have info about this food')
        break

    meal_weight = input('How many grams you eat? ')
    if meal_weight == 'q':
        break
    portion_meal = {"meal": meal, 'weight': int(meal_weight)}

    for food in data:
        if meal in food:
            food_intake[f"{portion_meal['meal']}"] = f"{portion_meal['weight']}"

            protein_intake += float(food[1]) * ((portion_meal.get('weight')) / 100)
            fat_intake += float(food[2]) * ((portion_meal.get('weight')) / 100)
            carbohydrate_intake += float(food[3]) * ((portion_meal.get('weight')) / 100)
            energy_intake += float(food[4]) * ((portion_meal.get('weight')) / 100)

print(f"Total nutrition intake:\n"
      f"\tProtein: {round(protein_intake, 2)} grams"
      f"\n\tFat: {round(fat_intake, 2)} grams"
      f"\n\tCarbohydrate: {round(carbohydrate_intake, 2)} grams"
      f"\n\tEnergy: {round(energy_intake, 2)} cal")
print(f"This meal you consume: {food_intake}")