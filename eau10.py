import sys


def searching_match(arg: str, element:str) -> bool:
    i: int = 0
    while i < len(arg):
        if i == len(element):
            return False
        if arg[i] != element[i]:
            return False
        i += 1
    if i < len(element):
        return False
    return True

def retrieving_element(array: tuple) -> int:
    counter: int = 0
    element: str = array[len(array) - 1]
    for arg in array[:len(array) - 1]:
        if searching_match(arg, element):
            return counter
        counter += 1
    return -1


def main(args: tuple) -> None:
    if len(args) < 3:
        print('error')
        sys.exit(1)

    index = retrieving_element(args[1:])

    print(index)


if __name__ == '__main__':
    main(sys.argv)
