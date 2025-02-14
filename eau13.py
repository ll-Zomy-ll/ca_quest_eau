import sys


def is_not_digit(args: tuple) -> bool:
    for arg in args:
        if not arg.isdigit():
            return True
    return False

def is_int(args: tuple) -> list:
    numbers: list = []
    for arg in args:
        numbers.append(int(arg))
    return numbers

def my_select_sort(array: list) -> list:
    array_length = len(array) - 1
    new_array: list = array
    for i in range(array_length):
        smallest = i
        for j in range(i + 1, array_length + 1):
            if new_array[j] < new_array[smallest]:
                smallest = j
        if smallest != i:
            new_array[i], new_array[smallest] = new_array[smallest], new_array[i]
    return new_array

def array_displaying(array: list) -> None:
    for element in array:
        print(element, end=' ')
    print()


def main(args: tuple) -> None:
    if len(args) < 3:
        print('error')
        sys.exit(1)
    if is_not_digit(args[1:]):
        print('error')
        sys.exit(1)

    new_array = my_select_sort(is_int(args[1:]))

    array_displaying(new_array)


if __name__ == '__main__':
    main(sys.argv)
