#!/usr/bin/env python3

# Dynamic programming is recursion + memoisation
#
# It works when the problem features both:
#
# Optimal substructure:
#    a globally optimal solution can be found by combining optimal
#    solutions to local subproblems
#    e.g. fib(x) = fib(x-1) + fib(x-2) for x > 1
#
# Overlapping subproblems:
#    finding an optimal solution involves solving the same problem
#    multiple times
def dynamic_fib(n, memo):
    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    result = dynamic_fib(n - 1, memo) + dynamic_fib(n - 2, memo)
    memo[n] = result
    return result


def recursive_fib(position):
    if position == 0 or position == 1:
        return 1
    else:
        return recursive_fib(position - 1) + recursive_fib(position - 2)


if __name__ == "__main__":
    print("Running {} tests:".format(__file__), end=' ')

    print("\n", dynamic_fib(120, {}))

    gts = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    for i in range(10):
        assert (recursive_fib(i) == gts[i])
        assert (recursive_fib(i) == dynamic_fib(i, {}))

    print("Passed")
