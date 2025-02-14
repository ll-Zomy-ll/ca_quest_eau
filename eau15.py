import sys


def main(args: tuple) -> None:
    if len(args) > 1:
        print('error')
        sys.exit(1)

    print('J\'ai terminé l\'Epreuve de l\'Eau et c\'était structurant.')


if __name__ == '__main__':
    main(sys.argv)
