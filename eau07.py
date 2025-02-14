import sys


def is_whitespace(char: str) -> bool:
    if (ord(char) == 9 or ord(char) == 10 or ord(char) == 32):
            return True
    return False

def upper_and_lowercasing(arg: str, i: int) -> str:
    word: str = ''
    first: int = 1
    while (i < len (arg) and not is_whitespace(arg[i])):
        if (arg[i].isalpha() and first == 1):
            word += arg[i].upper()
            first = 0
        elif (arg[i].isalpha() and first == 0):
            word +=  arg[i].lower()
        else:
            word += arg[i]
        i += 1
    return word

def parsing_string(arg: str) -> str:
    i: int = 0
    new_string: str = arg
    while i < len(arg):
        while is_whitespace(arg[i]):
            new_string = new_string[:i] + arg[i:]
            i += 1
        if not is_whitespace(arg[i]):
            word = upper_and_lowercasing(arg, i)
            new_string = new_string[:i] + word + arg[len(word) + i:]
            i += len(word)
    return new_string

def main(args: tuple) -> None:
    if len(args) != 2:
        print('error')
        sys.exit(1)
    if args[1].isdigit():
        print('error')
        sys.exit(1)

    new_string = parsing_string(args[1])

    print(new_string)


if __name__ == '__main__':
    main(sys.argv)
