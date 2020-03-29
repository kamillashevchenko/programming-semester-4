#!/usr/bin/python3

import random
import copy

def bubblesort(arr):
    for i in range(len(arr)):
         for j in range(len(arr)):
             if arr[i] > arr[j]:
                 arr[i], arr[j] = arr[j], arr[i]


def qsort(arr, first, last):
   if first >= last:
       return

   i, j = first, last
   pivot = arr[first]

   while i <= j:
       while arr[i] < pivot: i += 1
       while arr[j] > pivot: j -= 1
       if i <= j:
           arr[i], arr[j] = arr[j], arr[i]
           i, j = i + 1, j - 1
   qsort(arr, first, j)
   qsort(arr, i, last)


def print_arr(arr):
    for i, j in enumerate(arr):
        print(i, j)
    print()


def main(init_arr):
    arr = copy.copy(init_arr)
    bubblesort(arr)
    print_arr(arr)

    arr = copy.copy(init_arr)
    qsort(arr, 0, len(arr) - 1)
    print_arr(arr)


if __name__ == '__main__':
    numbers = []
    length = int(input())
    for i in range(length):
        numbers.append(int(input()))
    main(numbers)
