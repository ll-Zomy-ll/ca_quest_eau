import sys


def is_digit(args: tuple) -> bool:
    for arg in args:
        if ((arg[0] == '-' and len(arg) > 1) or arg[0].isdigit()):
            for char in arg[1:]:
                if not char.isdigit():
                    return False
        else:
            return False
    return True

def calculating_array(numbers: tuple) -> list:
    differences_list: list = []
    for number in range(len(numbers) - 1):
        for next_number in range(number + 1, len(numbers)):
            differences_list.append(abs(int(numbers[number]) - int(numbers[next_number])))
    return differences_list

def comparing_differences(differences_list: list) -> int:
    i: int = 1
    smallest = differences_list[0]
    while i < len(differences_list):
        if smallest > differences_list[i]:
            smallest = differences_list[i]
        i += 1
    return smallest


def main(args: tuple) -> None:
    if len(args) < 3:
        print('error')
        sys.exit(1)
    if not is_digit(args[1:]):
        print('error')
        sys.exit(1)

    differences_list = calculating_array(args[1:])

    smallest = comparing_differences(differences_list)

    print(smallest)


if __name__ == '__main__':
    main(sys.argv)
