"""
Problem 1: N-th Fibonacci Number
Write a program to compute the N-th Fibonacci number where:

F(0) = 0

F(1) = 1

F(n) = F(n-1) + F(n-2) for n ≥ 2

For example:

Input: n = 0
Output: 0

Input: n = 5
Output: 5
(Explanation: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5)

Input: n = 10
Output: 55
(Explanation: The sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

Constraints: 0 ≤ n ≤ 45
"""
from src.res.Practice.Recursion.fibonacci import input as ip, output as op


def solve():

    """
    The solution of the program
    :return: None
    """
    result = list()
    for n in ip.i_p:
        # result.append(fibonacci(n))
        # result.append(fibonacci_mem(n))
        result.append(fibonacci_tab(n))
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def fibonacci(num):
    """
    This function recursively calculates the factorial of a given number
    :param num: The number for which factorial is to be calculated
    :return: The factorial of the number
    """
    if num == 0 or num == 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_mem(num, memo=None):
    """
    This function solves fibonacci series using memoization
    :param num: The number for which the factorial is to be calculated
    :param memo: The cache used for storing results of subproblem
    :return: The factorial of the number
    """
    if memo is None:
        memo = {
            0: 0,
            1: 1
        }

    if num not in memo.keys():
        memo[num] = fibonacci_mem(num - 1, memo) + fibonacci_mem(num - 2, memo)

    return memo[num]


def fibonacci_tab(num):
    """
    This function solves fibonacci series using tabulation
    :param num: The number for which the factorial is to be calculated
    :return: The factorial of the number
    """
    if num == 0:
        return 0
    tab = [0] * (num + 1)
    tab[0], tab[1] = 0, 1

    for i in range(2, num + 1):
        tab[i] = tab[i-1] + tab[i-2]

    return tab[num]
