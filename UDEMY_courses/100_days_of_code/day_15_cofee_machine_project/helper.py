from drinks_resources import *

machine_profit = 0


def order_asking(source: dict):
    """Ask user for their order and return heir choice"""
    user_drink = int(input('What would you like? (expresso-(1)/ latte-(2)/ cappuccino-(3):\n'))
    for k, v in source.items():
        if user_drink == k:
            return v


# Turn of machine if enter 'off'
# print report if enter 'report'

# check resources sufficient
def check_resources_sufficient(drink: str):
    """Compare remain resources against drink recept"""
    water_needed = drink_recipes[drink]['water']
    coffee_needed = drink_recipes[drink]['coffee']
    milk_needed = drink_recipes[drink]['milk']

    remaining_water = resources['water']
    remaining_coffee = resources['coffee']
    remaining_milk = resources['milk']

    if water_needed > remaining_water:
        print(f'Sorry there is not enough water!')

    elif coffee_needed > remaining_coffee:
        print(f'Sorry there is not enough coffee!')

    elif milk_needed > remaining_milk:
        print(f'Sorry there is not enough milk!')

    else:
        return True


# process coins
def process_coins():
    """Ask user for coins. And return total sum"""
    user_cnt_coins = 0
    coins = ['quarter', 'dimes', 'nickles', 'pennies']

    while True:
        for coin in coins:
            # money_input - number of coin from each type
            money_input = input(f'Please insert number of coins - {coin}, or press (q) for quit coins insertion: ')

            if coin not in ['quarter', 'dimes', 'nickles', 'pennies', 'q']:
                print('Incorrect coin. Insert correct coin or q\n')
                continue
            else:
                if money_input != 'q':
                    user_cnt_coins += coins_dic[coin]*int(money_input)
                else:
                    break

        return round(user_cnt_coins, 2)


def is_transaction_successful(transaction, ordered_drink):
    drink_price = drink_prices[ordered_drink]

    if transaction < drink_price:
        print(f'\nSorry your transaction - ${transaction}. That is not enough money for {ordered_drink}-${drink_price}.\n'
              f'Money refunded')
    elif transaction == drink_price:
        pass # import way to add this sum to machine profit
        print(f"\nWait for your {ordered_drink}")

    else:
        print(f'\nHere is ${round((transaction-drink_price), 2)} dollars in change')


def order():
    my_order = order_asking(dic_drinks) # str

    if check_resources_sufficient(my_order):
        my_coin = process_coins()
        is_transaction_successful(my_coin, my_order)




