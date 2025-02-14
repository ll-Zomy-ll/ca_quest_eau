import sys


def ca_isdigit(arg: str) -> str:
    for char in arg:
        if (ord(char) < 48 or ord(char) > 57):
            return 'false'
    return 'true'


def main(args: tuple) -> None:
    if len(args) != 2:
        print('error')
        sys.exit(1)

    answer = ca_isdigit(args[1])

    print(answer)


if __name__ == '__main__':
    main(sys.argv)
