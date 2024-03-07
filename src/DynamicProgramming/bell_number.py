"""
Given a set of n elements, find number of ways of partitioning it.

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} }
            { {1, 2} }
Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }.

Bell(n) = k: 1->n Sum(S(n.k))
S(n+1,k) = k*S(n, k) + S(n, k-1)
S(n, k) = k*S(n-1, k) + S(n-1, k-1)
"""
from src.res.DynamicProgramming.bell_number import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(bell_number(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def bell_number(n):
    """
    This function returns the number of ways an array can be partitioned in.
    :arg n: The length of the array
    :return: The number of ways the array of length n can be partitioned
    """
    sum = 0
    for i in range(1, n+1):
        sum += calculate(n, i)
    return sum


def calculate(n, i):
    if i == 0 or i == 1 or n == 0 or n == 1:
        return 1
    return i*calculate(n-1, i) + calculate(n-1, i-1)