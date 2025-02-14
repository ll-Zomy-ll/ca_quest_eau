import sys


def sorting_elements(array: list, start: int, end: int) -> int:
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i

def my_partition_sort(array: list, start: int, end: int) -> list:
    if start < end:
        pivot: int = sorting_elements(array, start, end)
        my_partition_sort(array, start, pivot - 1)
        my_partition_sort(array, pivot + 1, end)
    return array

def displaying_array(array: list) -> None:
    for element in array:
        print(element, end=' ')
    print()


def main(args: tuple) -> None:
    if len(args) < 3:
        print('error')
        sys.exit(1)

    new_array: list = my_partition_sort(list(args[1:]), 0, len(args[1:]) - 1)

    displaying_array(new_array)



if __name__ == '__main__':
    main(sys.argv)
