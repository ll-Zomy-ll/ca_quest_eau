import sys


def displaying_args() -> None:
    args: tuple = sys.argv[1:]
    for i in range(len(args) - 1, -1, -1):
        print(args[i])


def main() -> None:
    if len(sys.argv) <= 1:
        print("This program needs arguments to operate")
        sys.exit(1)

    displaying_args()


if __name__ == '__main__':
    main()
