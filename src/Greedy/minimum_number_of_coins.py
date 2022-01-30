"""
Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in
Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is
the minimum number of coins and/or notes needed to make the change?

Input: V = 70
Output: 2
We need a 50 Rs note and a 20 Rs note.

Input: V = 121
Output: 3
We need a 100 Rs note, a 20 Rs note and a 1 Rs coin.
"""
from src.res.Greedy.minimum_number_of_coins import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    result = min_number_of_coins(arr, denominations)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def min_number_of_coins(amount, denominations):
    """
    To return the minimum number of coins for the amount
    :param amount: total amount of sum
    :param denominations: list of allowed denominations
    :return: minimum number of coins required
    """
    result = 0
    count = []
    denominations.sort(reverse=True)
    for d in denominations:
        c = amount // d
        amount = amount - (c*d)
        count.append(c)
    for c in count:
        result += c
    return result
