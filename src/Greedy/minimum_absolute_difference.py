"""
The absolute difference is the positive difference between two values a and b, is written |a-b| or |b-a| and they are
equal. If a=3 and b = 2, |3-2| = |2-3} = 1 . Given an array of integers, find the minimum absolute difference between
any two elements in the array.
"""
from src.res.Greedy.minimum_absolute_difference import input as ip, output as op


def minimum_absolute_difference(arr):
    """
    To find the minimum absolute between all pairs of elements of a list
    :param arr: the list
    :return: the minimum absolute difference
    """
    arr.sort()
    min_diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff


def solve():
    """
    The solution of the program
    :return: None
    """
    n = ip.n
    l = ip.arr
    result = minimum_absolute_difference(l)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)
