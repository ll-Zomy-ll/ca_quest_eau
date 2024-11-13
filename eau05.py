import sys


def ca_len(arg) -> int:
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(av: tuple) -> bool:
    for arg in av:
        if ((arg[0] == '-' and ca_len(arg) > 1) or (ord(arg[0]) >= 48
             and ord(arg[0]) <=57)):
            for i in arg[1:]:
                if (ord(i) < 48 or ord(i) > 57):
                    return False
        else:
            return False
    return True

def searching_str(long_str, small_str, ls_len: int, sm_len: int) -> bool:
    i: int = 0
    while i < ls_len:
        j = 0
        if long_str[i] == small_str[j]:
            while (j < sm_len and i + j < ls_len):
                if long_str[i + j] != small_str[j]:
                    j = sm_len
                if j == sm_len - 1:
                    return True
                j += 1
        i += 1
    return False


def main(av: tuple) -> None:
    if searching_str(av[0], av[1], ca_len(av[0]), ca_len(av[1])):
        print("true")
    else:
        print("false")


if __name__ == '__main__':
    if (ca_len(sys.argv) == 3 and not ca_isdigit(sys.argv[1:])):
        main(sys.argv[1:])
    else:
        print("error")
