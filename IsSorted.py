#!/usr/bin/env python3


def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    unsorted = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

    assert (not is_sorted(unsorted))

    sorted = [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]

    assert (is_sorted(sorted))

    print("Passed")
