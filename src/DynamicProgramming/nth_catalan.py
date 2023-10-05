"""
Catalan numbers are defined as a mathematical sequence that consists of positive integers, which can be used to find the
number of possibilities of various combinations.

The nth term in the sequence denoted Cn, is found in the following formula: (2n)!/((n + 1)! n!)

The first few Catalan numbers for n = 0, 1, 2, 3, … are : 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
"""
from ..res.DynamicProgramming.nth_catalan import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        if n <= 1:
            results.append(1)
        else:
            results.append(catalan(n))
        # results.append(catalan(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def catalan(n):
    """
    This function calculates and returns the nth catalan number
    :arg n: The nth term to be calculated
    :return: the nth catalan number
    """
    fact_list = [-1] * (2*n+1)
    fact_list[0] = 1
    return factorial(2*n, fact_list) / (factorial(n+1, fact_list) * factorial(n, fact_list))


def factorial(n, fact_list):
    """
    This function calculates and returns the factorial of a number
    :args n: The number for which the factorial is to be found
    :return: The factorial of the number
    """
    if fact_list[n] == -1:
        fact_list[n] = n * factorial(n-1, fact_list)
    return fact_list[n]
