"""
You are given a staircase with n steps. Each time you move, you can climb either 1 or 2 steps. The task is to find how
many distinct ways you can climb to the top of the staircase.

Sample Input and Output

| Input | Output | Explanation                                       |
| ----- | ------ | ------------------------------------------------- |
| n = 2 | 2      | Ways: [1+1],                                      |
| n = 3 | 3      | Ways: [1+1+1], [1+2], [2+1]                       |
| n = 4 | 5      | Ways: [1+1+1+1], [1+2+1], [1+1+2], [2+1+1], [2+2] |

Order matters in each sequence of steps.
"""
from src.res.DynamicProgramming.climbing_stairs import input as ip, output as op

def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(climbing_stairs_recursion(n))
        # results.append(climbing_stairs_memoization(n))
        results.append(climbing_stairs_tabulation(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def climbing_stairs_recursion(n):
    """
    This function finds the number of ways a stair of n steps can be climbed using recursion
    :param n: The number of steps on the stairs
    :type n: int
    :return: The number of ways of climbing n-stepped stairs
    :rtype: int
    """
    if n == 1 or n == 2:
        return n
    return climbing_stairs_recursion(n-1) + climbing_stairs_recursion(n-2)


def climbing_stairs_memoization(n, mem=None):
    """
    This function finds the number of ways a stair of n steps can be climbed using memoization
    :param n: The number of steps on the stairs
    :type n: int
    :param mem: cache to store solutions of intermediate problems
    :type mem: array; int
    :return: numbers of ways a stairs of n-steps can be climbed
    :rtype: int
    """
    if n == 0:
        return n
    if mem is None:
        mem = {
            1: 1,
            2: 2
        }

    if n not in mem.keys():
        mem[n] = climbing_stairs_memoization(n-1, mem) + climbing_stairs_memoization(n-2, mem)
    return mem[n]


def climbing_stairs_tabulation(n):
    """
    This function finds the number of ways a stair of n steps can be climbed using memoization
    :param n: The number of steps on the stairs
    :type n: int
    :return: numbers of ways a stairs of n-steps can be climbed
    :rtype: int
    """
    if n == 0 or n == 1:
        return n
    tab = [0] * (n)
    tab[0], tab[1] = 1, 2

    for i in range(2, n):
        tab[i] = climbing_stairs_tabulation(n-1) + climbing_stairs_tabulation(n-2)

    return tab[n - 1]
