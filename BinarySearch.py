#!/usr/bin/env python3


def binary_search(input_array, value):
    upper = len(input_array) - 1
    lower = 0
    while lower <= upper:
        mid = (upper + lower) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1


if __name__ == "__main__":
    print("Running {} tests".format(__file__))

    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    test_val3 = 29
    test_val4 = 1
    assert(binary_search(test_list, test_val1) == -1)
    assert(binary_search(test_list, test_val2) == 4)
    assert(binary_search(test_list, test_val3) == 6)
    assert(binary_search(test_list, test_val4) == 0)
