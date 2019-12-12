#!/usr/bin/env python3

from IsSorted import is_sorted


def bubble_sort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n):

        # Allows us to exit early when no swap has occurred
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element is greater than the next one
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            print(i, "Exit early")
            return


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

    assert (not is_sorted(array))

    bubble_sort(array)

    assert (is_sorted(array))

    sorted = [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]

    assert (is_sorted(sorted))

    bubble_sort(sorted)

    assert (is_sorted(sorted))

    almost_sorted = [1, 3, 4, 14, 9, 6, 20, 21, 21, 25]

    assert (not is_sorted(almost_sorted))

    bubble_sort(almost_sorted)

    assert (is_sorted(almost_sorted))

    print("Passed")
