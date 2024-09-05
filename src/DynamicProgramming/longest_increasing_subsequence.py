"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""
from src.res.DynamicProgramming.longest_increasing_subsequence import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    i_p = ip.i_p
    results = []
    for arr in i_p:
        results = longest_increasing_subsequence_dp(arr)
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def longest_increasing_subsequence_dp(arr):
    """
    This function finds the longest increasing subsequence in a list
    :param arr: The list
    :return: length of the longest increasing subsequence
    """
    lis = [1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    return max(lis)

