"""
Catalan numbers are defined as a mathematical sequence that consists of positive integers, which can be used to find the
number of possibilities of various combinations.

The nth term in the sequence denoted Cn, is found in the following formula:
Factorial definition: (2n)!/((n + 1)! n!)
Recursive definition: C(0) = 1 and C(n+1) = Sum {i=0 to n} C(i)C(n-1) for n >= 0

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

    print('Factorial Approach:')
    for n in arr:
        results.append(catalan_factorial(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)

    results = []
    print('Recursive Approach:')
    for n in arr:
        results.append(catalan_recursive(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def catalan_factorial(n):
    """
    This function calculates and returns the nth catalan number using factorial definition
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
    :args fact_list: memoized list of factorial
    :return: The factorial of the number
    """
    if fact_list[n] == -1:
        fact_list[n] = n * factorial(n-1, fact_list)
    return fact_list[n]


def catalan_recursive(n):
    """
    This function calculates and return the nth catalan using recursive definition
    :args n
    """
    recur_list = [-1] * (n+1)
    recur_list[0] = 1
    # catalan_sum = 0
    # for i in range(n):
    #     catalan_sum += catalan(i, recur_list) * catalan(n-i-1, recur_list)
    return catalan(n, recur_list)


def catalan(n, recur_list):
    """
    This function calculates the intermediate step of catalan sum
    :args n: The number for which the intermediate value is calculated
    :args fact_list: memoized list of recursion
    """
    if recur_list[n] == -1:
        catalan_sum = 0
        for i in range(n):
            catalan_sum += catalan(i, recur_list) * catalan(n - i - 1, recur_list)
        recur_list[n] = catalan_sum
    return recur_list[n]
