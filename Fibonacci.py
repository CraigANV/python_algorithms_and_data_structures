#!/usr/bin/env python3


def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


if __name__ == "__main__":
    print("Running {} tests".format(__file__))

    # Test cases
    assert(get_fib(0) == 0)
    assert(get_fib(1) == 1)
    assert(get_fib(2) == 1)
    assert(get_fib(3) == 2)
    assert(get_fib(4) == 3)
    assert(get_fib(5) == 5)
    assert(get_fib(6) == 8)
    assert(get_fib(7) == 13)
    assert(get_fib(8) == 21)
    assert(get_fib(9) == 34)
    assert(get_fib(11) == 89)
