import sys


def is_digit(args: tuple) -> bool:
    for arg in args:
        if not arg.isdigit():
            return False
    return True

def min_and_max(numbers: tuple) -> int:
    first: int = int(numbers[0])
    second: int = int(numbers[1])
    if first < second:
        min = first
        max = second
    else:
        min = second
        max = first
    return (min, max)

def parsing_numbers(numbers: tuple) -> list:
    values: list = []
    min, max = min_and_max(numbers)
    for i in range(max - min):
        values.append(min + i)
    return values

def displaying_values(values: list) -> None:
    for number in values:
        print(number, end=' ')
    print()


def main(args: tuple) -> None:
    if len(args) != 3:
        print('error')
        sys.exit(1)
    if not is_digit(args[1:]):
        print('error')
        sys.exit(1)

    values = parsing_numbers(args[1:])

    displaying_values(values)


if __name__ == '__main__':
    main(sys.argv)
