import sys


def ca_len(arg) -> int:
    length: int = 0
    for i in arg:
        length += 1
    return length

# Parsing + result display
'''Return a list of ascending numbers who are formed of 3 ascending numbers.'''
def main() -> None:
    i: int = 0
    while i <= 9:
        j = i + 1
        while j <= 9:
            k = j + 1
            while k <= 9:
                if (i < j and j < k):
                    print(f"{i}{j}{k}", end='')
                    if i != 7:
                        print(", ", end='')
                k += 1
            j += 1
        i += 1
    print()


# Error handling 
if __name__ == '__main__':
    if ca_len(sys.argv) == 1:
        main()
    else:
        print("Just turn on the program")
