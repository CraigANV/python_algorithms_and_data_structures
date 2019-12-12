#!/usr/bin/env python3

from IsSorted import is_sorted


# Takes the last element of an array as the pivot, and moves all
# elements smaller to the left of it and all larger to the right
def partition(array, lo, hi):
    pivot = array[hi]

    i = (lo - 1)  # index of smaller element

    for j in range(lo, hi):

        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[hi] = array[hi], array[i + 1]
    return i + 1


def quicksort(array, lo, hi):
    if lo < hi:
        # pi is partitioning index
        # after this arr[pi] is in correct position
        pi = partition(array, lo, hi)

        # Separately sort elements before
        # partition and after partition
        quicksort(array, lo, pi - 1)
        quicksort(array, pi + 1, hi)


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    assert (not is_sorted(array))

    quicksort(array, 0, len(array) - 1)

    assert (is_sorted(array))

    print("Passed")
