import sys


def ca_len(arg) -> int:
    length:int = 0
    for i in arg:
        length += 1
    return length


# Parsing + result display
def main(av: tuple) -> None:
    for i in range(ca_len(av) - 1, -1, -1):
        print(av[i])


# Error handling
if __name__ == '__main__':
    if ca_len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print("This program needs arguments to operate")
