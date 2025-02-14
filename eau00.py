import sys


def parsing_combinations() -> list:
    '''Return a list of ascending numbers who are formed of 3 ascending numbers.'''
    i: int = 0
    combinations_list: list = []
    while i <= 9:
        j = i + 1
        while j <= 9:
            k = j + 1
            while k <= 9:
                combination = 0
                if (i < j and j < k):
                    combination = i * 100 + j * 10 + k
                    combinations_list.append(combination)
                k += 1
            j += 1
        i += 1
    return combinations_list

def displaying_combinations(combinations_list: list) -> None:
    '''Print every possible combination of three ascending numbers  '''
    for combination in combinations_list:
        print(f'{combination:03d}', end='')
        if combination != 789:
            print(", ", end='')
    print()


def main(args: tuple) -> None:
    if len(args) != 1:
        print("Just turn on the program")
        sys.exit(1)

    combinations_list = parsing_combinations()

    displaying_combinations(combinations_list)


if __name__ == '__main__':
    main(sys.argv)
