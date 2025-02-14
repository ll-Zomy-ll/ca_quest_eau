import sys


def parsing_combinations() -> list:
    i: int = 0
    combinations_list: list = []
    while i < 99:
        j = i + 1
        while j <= 99:
            combinations_list.append(f'{i:02d} {j:02d}')
            j += 1
        i += 1
    return combinations_list

def displaying_combinations(combinations_list: list) -> None:
    for combination in combinations_list:
        print(f'{combination}', end='')
        if combination != '98 99':
            print(", ", end='')
    print()


def main() -> None:
    if len(sys.argv) != 1:
        print("Just turn on the program")
        sys.exit(1)

    combinations_list = parsing_combinations()

    displaying_combinations(combinations_list)


if __name__ == '__main__':
    main()
