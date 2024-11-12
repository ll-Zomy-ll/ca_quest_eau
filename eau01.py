import sys


def ca_len(arg) -> int:
    length: int = 0
    for i in arg:
        length += 1
    return length


# Parsing + result display
def main() -> None:
    i: int = 0
    while i < 99:
        j = i + 1
        while j <= 99:
            print(f"{i:02d} {j:02d}", end='')
            if i != 98:
                print(", ", end='')
            j += 1
        i += 1
    print()


# Error handling
if __name__ == '__main__':
    if ca_len(sys.argv) == 1:
        main()
    else:
        print("Just turn on the program")
