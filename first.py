#!/usr/bin/python3
""" task 27 """

import copy

def bubblesort(arr):
    """ bubble sort """
    for idx, _ in enumerate(arr):
        for j, _ in enumerate(arr):
            if arr[idx] > arr[j]:
                arr[idx], arr[j] = arr[j], arr[idx]


def qsort(arr, first, last):
    """ quick sort """
    if first >= last:
        return

    idx, j = first, last
    pivot = arr[first]

    while idx <= j:
        while arr[idx] < pivot:
            idx += 1
        while arr[j] > pivot:
            j -= 1
        if idx <= j:
            arr[idx], arr[j] = arr[j], arr[idx]
            idx, j = idx + 1, j - 1
    qsort(arr, first, j)
    qsort(arr, idx, last)


def print_arr(arr):
    """ print array """
    for idx, j in enumerate(arr):
        print(idx, j)
    print()


def main(init_arr):
    """ main """
    arr = copy.copy(init_arr)
    bubblesort(arr)
    print_arr(arr)

    arr = copy.copy(init_arr)
    qsort(arr, 0, len(arr) - 1)
    print_arr(arr)


if __name__ == '__main__':
    NUMBERS = []
    LENGTH = int(input())
    for k in range(LENGTH):
        NUMBERS.append(int(input()))
    main(NUMBERS)
