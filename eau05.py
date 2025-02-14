import sys


def is_digit() -> bool:
    for i in range(1, 3):
        if sys.argv[i].isdigit():
            return True
    return False

def searching_str(long_str, small_str) -> str:
    i: int = 0
    long_len: int = len(long_str)
    small_len: int = len(small_str)
    while i < long_len:
        j = 0
        if long_str[i] == small_str[j]:
            while (j < small_len and i + j < long_len):
                if long_str[i + j] != small_str[j]:
                    j = small_len
                if j == small_len - 1:
                    return 'true'
                j += 1
        i += 1
    return 'false'


def main() -> None:
    if len(sys.argv) != 3:
        print("error")
        sys.exit(1)
    if is_digit():
        print("error")
        sys.exit(1)

    answer: str = searching_str(sys.argv[1], sys.argv[2])

    print(answer)


if __name__ == '__main__':
    main()
