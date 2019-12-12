#!/usr/bin/env python3

from IsSorted import is_sorted


def merge(array, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1


def mergesort(array):
    n = len(array)
    if n < 2:
        return

    mid = n // 2
    left = array[0: mid]
    right = array[mid:n]

    mergesort(left)
    mergesort(right)

    merge(array, left, right)


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    array = [21, 4, 1, 3, 9, 20, 25]
    assert (not is_sorted(array))

    mergesort(array)

    assert (is_sorted(array))

    print("Passed")
