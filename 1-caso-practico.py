def main():
    product_name = input('Please, enter the name of the product: ')
    weight_string = input('Please, enter the weight of the product in kilograms: ')
    print('\n' * 2)

    weight = float(weight_string)
    weight_two_decimals = round(weight, 2)

    print(f'The weight of {product_name} is {weight_two_decimals} kg')
    print('\n' * 2 + 'Done. PROGRAMMER!')


if __name__ == "__main__":
    main()