import sys


def ca_len(arg) -> int:
    length:int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(arg: str) -> bool:
    for i in arg:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    return True


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
    return 0


def main(av: int) -> None:
    prime: int = generating(av)
    if prime:
        print(prime)
    else:
        print("The number is too long.")


if __name__ == '__main__':
    if (ca_len(sys.argv) == 2 and ca_isdigit(sys.argv[1])):
        main(int(sys.argv[1]))
    else:
        print("-1")
