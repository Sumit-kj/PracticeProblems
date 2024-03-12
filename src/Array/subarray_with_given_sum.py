"""
Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.

Note: There may be more than one subarray with sum as the given sum, print first such subarray.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Output: Sum found between indexes 1 and 4
Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
Explanation: There is no subarray with 0 sum
"""
from src.res.Array.subarray_with_given_sum import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(subarray_with_given_sum(n[0], n[1]))
        results.append(subarray_with_given_sum_sliding_window(n[0], n[1]))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def subarray_with_given_sum(arr, sum_key):
    """
    This function returns the first set of indices that equals the given sum
    Args:
        arr: The list of elements in which the sum is to be found
        sum_key: The sum to be found
    Returns:
        The first and last index of the subarray
    """
    arr_len = len(arr)
    start, end = -1, -1
    for i in range(arr_len - 1):
        inter_sum = arr[i]
        j = i + 1
        while j < arr_len and inter_sum < sum_key:
            inter_sum += arr[j]
            j += 1
        if inter_sum == sum_key:
            start, end = i, j - 1
    return start, end


def subarray_with_given_sum_sliding_window(arr, sum_key):

    """
    This function returns the first set of indices that equals the given sum
    Args:
        arr: The list of elements in which the sum is to be found
        sum_key: The sum to be found
    Returns:
        The first and last index of the subarray
    """
    start, current_sum = 0, arr[0]
    i = 1
    while start < i < len(arr):
        if current_sum == sum_key:
            return start, i - 1
        if current_sum > sum_key:
            current_sum -= arr[start]
            start += 1
            continue
        else:
            current_sum += arr[i]
            i += 1
    return -1, -1
