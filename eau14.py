import sys


def sorting_elements(array: list, start: int, end: int) -> int:
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1
    array[i], array[end] = array[end], array[i]
    return i

def partitionning_array(array: list, start: int, end: int) -> list:
    if start < end:
        smallest = sorting_elements(array, start, end)
        partitionning_array(array, start, smallest - 1)
        partitionning_array(array, smallest + 1, end)
    return array

def my_select_sort(array: tuple) -> list:
    new_array: list = partitionning_array(list(array), 0, len(array) - 1)
    return new_array

def displaying_array(array: list) -> None:
    for element in array:
        print(element, end=' ')
    print()


def main(args: tuple) -> None:
    if len(args) < 3:
        print('error')
        sys.exit(1)

    new_array: list = my_select_sort(args[1:])

    displaying_array(new_array)



if __name__ == '__main__':
    main(sys.argv)
