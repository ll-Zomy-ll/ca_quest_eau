import sys


def parsing_element(index: int) -> int:
    if index == 0:
        return 0
    if index == 1:
        return 1
    i: int = 1
    fn_1: int = 1
    fn_2: int = 0
    while i < index:
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
        i += 1
    return fn


def main() -> None:
    if len(sys.argv) != 2:
        print("-1")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("-1")
        sys.exit(1)
    
    element: int = parsing_element(int(sys.argv[1]))

    print(element)


if __name__ == '__main__':
    main()
