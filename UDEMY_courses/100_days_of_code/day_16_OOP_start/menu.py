class DrinksResources:
    resources = {
        'water': 300,
        'milk': 200,
        'coffee': 200,
        'money': 0
    }

    drink_recipes = {
        'expresso': {'water': 50, 'coffee': 18, 'milk': 0},
        'latte': {'water': 200, 'coffee': 24, 'milk': 150},
        'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100}
    }

    dic_drinks = {1: 'expresso', 2: 'latte', 3: 'cappuccino'}

    drink_prices = {'expresso': 1.5, 'latte': 2.5, 'cappuccino': 3}
    coins_dic = {'quarter': 0.25, 'dimes': 0.1, 'nickles': 0.05, 'pennies': 0.01}


    def order_asking(self, ):
        """Ask user for their order and return heir choice"""
        user_drink = input('What would you like? (expresso-(1)/ latte-(2)/ cappuccino-(3):\n')

        if user_drink == 'report':
            return 'report'
        elif user_drink == 'end':
            return 'end'

        elif user_drink != 'report' or 'end':
            for k, v in dic_drinks.items():
                if int(user_drink) == k:
                    return v
