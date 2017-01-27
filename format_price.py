import argparse
import re


def get_price_from_terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument("price", help="Price which you want to format", type=str)
    args = parser.parse_args()
    return args.price

def convert_string_to_number(string):
    string = string.replace(',','.')
    number = float(string)
    return (int(number) if number.is_integer() else number)

def format_price(price=None):
    if isinstance(price, int) and (price >= 0):
        return "{:,}".format(price).replace(",", " ")
    elif isinstance(price, float) and (price >= 0):
        return (format_price(int(price)) if price.is_integer() 
                else "{:,.2f}".format(price).replace(",", " "))
    elif isinstance(price, str) and re.match(r'\d+[\.,]?\d*$', price):
        price = convert_string_to_number(price)
        return format_price(price)
    else:
        raise ValueError

def main():
    price = get_price_from_terminal()
    print(format_price(price))


if __name__ == '__main__':
    main()