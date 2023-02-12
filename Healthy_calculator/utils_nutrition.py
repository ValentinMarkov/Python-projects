class Product:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'Product name: {self.name}'

    def product_nutrition_values(self):
        """Get nutrition values from csv"""

        list_values = [line.rstrip('\n') for line in open('food_data.csv')]  # Read the file

        food_dct = {}  # Transform in dictionary --> 'oats': ['13', '6.5', '68', '379']

        for item in list_values:
            food_dct[item.split(',')[0]] = item.split(',')[1:]

        for k, v in food_dct.items():
            if k == self.name:
                return v

    def calculation_nutrition(self):
        """Calculate nutrition values per product weight"""
        product_nutrition_values = Product.product_nutrition_values(self)
        protein = round(((float(product_nutrition_values[0]) / 100) * self.weight), 1)
        fat = round(((float(product_nutrition_values[1]) / 100) * self.weight), 1)
        carbohydrate = round(((float(product_nutrition_values[2]) / 100) * self.weight), 1)
        energy = round(((float(product_nutrition_values[3]) / 100) * self.weight), 1)

        return protein, fat, carbohydrate, energy

    def print_results(self):
        """Print readable info"""
        print('* ' * 30)
        print(f'Total proteins: {Product.calculation_nutrition(self)[0]}\n'
              f'Total fat: {Product.calculation_nutrition(self)[1]}\n'
              f'Total carbohydrate: {Product.calculation_nutrition(self)[2]}\n'
              f'Total energy: {Product.calculation_nutrition(self)[3]}\n'
              )
