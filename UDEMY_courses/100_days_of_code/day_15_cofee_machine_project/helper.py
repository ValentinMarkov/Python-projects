from drinks_resources import *

machine_profit = 0


def order_asking(source: dict):
    """Ask user for their order and return heir choice"""
    user_drink = input('What would you like? (expresso-(1)/ latte-(2)/ cappuccino-(3):\n')

    if user_drink == 'report':
        return 'report'
    elif user_drink == 'end':
        return 'end'

    elif user_drink != 'report' or 'end':
        for k, v in source.items():
            if int(user_drink) == k:
                return v


def print_report():
    """Print report if needed"""
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${round(resources['money'],2)}")


# check resources sufficient
def check_resources_sufficient(drink: str):
    """Compare remain resources against drink recept"""
    resources_sufficient = True

    water_needed = drink_recipes[drink]['water']
    coffee_needed = drink_recipes[drink]['coffee']
    milk_needed = drink_recipes[drink]['milk']

    remaining_water = resources['water']
    remaining_coffee = resources['coffee']
    remaining_milk = resources['milk']

    if water_needed > remaining_water:
        print(f'Sorry there is not enough water!')
        resources_sufficient = False

    elif coffee_needed > remaining_coffee:
        print(f'Sorry there is not enough coffee!')
        resources_sufficient = False

    elif milk_needed > remaining_milk:
        print(f'Sorry there is not enough milk!')
        resources_sufficient = False

    else:
        return resources_sufficient


# process coins
def process_coins():
    """Ask user for coins. And return total sum"""
    user_cnt_coins = 0
    coins = ['quarter', 'dimes', 'nickles', 'pennies']

    while True:
        for coin in coins:
            # money_input - number of coin from each type
            money_input = input(f'Please insert number of coins - {coin}, or press (q) for quit coins insertion: ')

            if money_input == 'report':
                return 'report'

            elif money_input == 'end':
                return 'end'

            elif coin not in ['quarter', 'dimes', 'nickles', 'pennies', 'q']:
                print('Incorrect coin. Insert correct coin or q\n')
                continue
            else:
                if money_input != 'q':
                    user_cnt_coins += coins_dic[coin] * int(money_input)
                else:
                    break

        return round(user_cnt_coins, 2)


def is_transaction_successful(transaction, ordered_drink):
    """Check sum of coin"""
    drink_price = drink_prices[ordered_drink]
    transaction_successful = True

    if transaction < drink_price:
        print(
            f'\nSorry your transaction - ${transaction}. That is not enough money for {ordered_drink}-${drink_price}.\n'
            f'Money refunded')
        transaction_successful = False

    elif transaction == drink_price:
        print(f"\nWait for your {ordered_drink}...")
        resources['money'] += drink_price
    else:
        print(f'\nHere is ${round((transaction - drink_price), 2)} dollars in change')
        print(f"\nWait for your {ordered_drink}...")
        resources['money'] += drink_price

    return transaction_successful


def make_drinks(ordered_drinks: str):
    """Create drink and decrease remain resources"""
    water_needed = drink_recipes[ordered_drinks]['water']
    coffee_needed = drink_recipes[ordered_drinks]['coffee']
    milk_needed = drink_recipes[ordered_drinks]['milk']

    resources['water'] -= water_needed
    resources['coffee'] -= coffee_needed
    resources['milk'] -= milk_needed

    print(f'Here is your {ordered_drinks}. Enjoy!')


def order():
    while True:
        my_order = order_asking(dic_drinks)
        if my_order == 'report':
            print_report()
            continue
        elif my_order == 'end':
            print('Machin is shut down. . .')
            break

        if check_resources_sufficient(my_order):
            my_coin = process_coins()
        else:
            break

        if my_coin == 'end':
            print('Machin is shut down. . .')
            break

        elif my_coin == 'report':
            print_report()
            break

        if is_transaction_successful(my_coin, my_order):
            make_drinks(my_order)
        else:
            break


