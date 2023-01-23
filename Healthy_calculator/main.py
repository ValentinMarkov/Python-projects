from utils_nutrition import Product

if __name__ == "__main__":
    prod_name = input(f'Product name: ')
    prod_weight = float(input(f'Product weight: '))

    prod_1 = Product(prod_name, prod_weight)
    print(Product.calculation_nutrition(prod_1))