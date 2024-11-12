import sys


def ca_len(arg) -> int:
    length: int = 0
    for i in arg:
        length += 1
    return length

def ca_isdigit(arg: str) -> bool:
    for i in arg:
        if (ord(i) < 48 or ord(i) > 57):
            return False
    return True


# Parsing + result display
def main(index) -> None:
    if index == '0':
        print('0')
        return
    if index == '1':
        print('1')
        return
    i: int = 1
    fn_1: int = 1
    fn_2: int = 0
    while i < int(index):
        fn = fn_1 + fn_2
        fn_2 = fn_1
        fn_1 = fn
        i += 1
    print(fn)



# Error handling
if __name__ == '__main__':
    if (ca_len(sys.argv) == 2 and ca_isdigit(sys.argv[1])):
        main(sys.argv[1])
    else:
        print("-1")
