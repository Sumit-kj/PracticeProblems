"""
The factorial problem asks you to find the product of all positive integers from 1 up to a given non-negative integer
$$ n $$. This means you want to determine how many ways things can be arranged or multiplied in a sequence running from
1 all the way to $$ n $$.

For example, if you pick n = 5, the factorial of 5 (written as 5!) is the multiplication of 1 × 2 × 3 × 4 × 5.
This kind of operation is common in counting problems—like how many ways you can arrange a set of items or calculate
permutations.
"""
from src.res.Practice.Recursion.factorial import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    result = list()
    for n in ip.i_p:
        # result.append(factorial(n))
        # result.append(factorial_memo(n))
        result.append(factorial_tab(n))
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def factorial(num):
    """
    This function recursively calculates the factorial of a given number
    :param num: The number for which factorial is to be calculated
    :return: The factorial of the number
    """
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def factorial_memo(num, memo=None):
    """
    This function solves the factorial problem using the memoization technique
    :param num: The number for which the factorial is to be calculated
    :param memo: This is the memoization cache for storing the solutions to subproblems
    :return: Factorial of the number
    """
    if memo is None:
        memo = {
            0: 1
        }

    if num in memo.keys():
        return memo[num]

    res = num * factorial_memo(num-1, memo)
    memo[num] = res
    return res


def factorial_tab(num):
    """
    This function solves the factorial problem using tabulation technique
    :param num: The number of which the factorial is to be calculated
    :return: Factorial of the number
    """
    tab = [0] * (num + 1)
    tab[0] = 1

    for i in range(1, num + 1):
        tab[i] = i * tab[i-1]

    return tab[num]
