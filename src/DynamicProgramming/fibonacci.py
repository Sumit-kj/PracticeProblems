"""
The Fibonacci numbers are the numbers in the following integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
"""
from ..res.DynamicProgramming.fibonacci import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        fib_list = [-1] * (n + 1)
        fib_list[0], fib_list[1] = 0, 1
        results.append(fibonacci(n, fib_list))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def fibonacci(n, fib_list):
    """
    This function calculates and returns nth number ijn fibonacci series
    :args n: The index in fibonacci series to be calculated
    :args fib_list: The memoization list of fibonacci series
    :return: The nth fibonacci number
    """
    if fib_list[n] == -1:
        return fibonacci(n-1, fib_list) + fibonacci(n-2, fib_list)
    return fib_list[n]
