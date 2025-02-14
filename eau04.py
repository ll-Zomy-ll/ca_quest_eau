import sys


def generating(nbr: int) -> int:
    i: int = 1
    prime: int = 0
    while nbr + i < 100000000:
        j = 2
        if ((nbr + i != 3 and (nbr + i) % 3 == 0) or (nbr + i != 5
             and (nbr + i) % 5 == 0)):
            i += 1
        while j <= nbr + i:
            prime = 1
            if (j != nbr + i and (nbr + i) % j == 0):
                prime = 0
                j = nbr + i
            j += 1
        if prime:
            return nbr + i
        if (nbr + i != 1 and (nbr + i) % 2 != 0):
            i += 1
        i += 1
    return -1


def main() -> None:
    if len(sys.argv) != 2:
        print("-1")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("-1")
        sys.exit(1)

    prime: int = generating(int(sys.argv[1]))

    print(prime)


if __name__ == '__main__':
    main()
