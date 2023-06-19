import argparse
from src.calculator import add_numbers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add two numbers.')
    parser.add_argument('num1', type=int, help='First number')
    parser.add_argument('num2', type=int, help='Second number')
    args = parser.parse_args()

    result = add_numbers(args.num1, args.num2)
    print('The sum of {} and {} is: {}'.format(args.num1, args.num2, result))