import sys


def lowercasing(char: str) -> str:
    if (ord(char) >= 65 and ord(char) <= 90):
        char = chr(ord(char) + 32)
    return char

def uppercasing(char: str) -> str:
    if (ord(char) >= 97 and ord(char) <= 122):
        char = chr(ord(char) - 32)
    return char

def parsing_letters(arg: str) -> str:
    odd: int = 1
    for i in range(len(arg)):
        if (arg[i].isalpha() and odd == 1):
            char = uppercasing(arg[i])
            if i == 0:
                string = char + arg[i + 1:]
            else:
                string = string[:i] + char + arg[i + 1:]
            odd = 0
        elif (arg[i].isalpha() and odd == 0):
            char = lowercasing(arg[i])
            string = string[:i] + char + arg[i + 1:]
            odd = 1
    return string


def main(args: tuple) -> None:
    if len(args) != 2:
        print('error')
        sys.exit(1)
    if args[1].isdigit():
        print('error')
        sys.exit(1)

    string = parsing_letters(args[1])

    print(string)


if __name__ == '__main__':
    main(sys.argv)
