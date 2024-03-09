"""
Given an array arr[] of integers, segregate even and odd numbers in the array such that all the even numbers should be
present first, and then the odd numbers.

Examples:

Input: arr[] = {7, 2, 9, 4, 6, 1, 3, 8, 5}
Output: 2 4 6 8 7 9 1 3 5

Input: arr[] = {1, 3, 2, 4, 7, 6, 9, 10}
Output:  2 4 6 10 7 1 9 3
"""
from src.res.Array.segregate_even_odd import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(segregate_even_odd(n))
    print(results)


def segregate_even_odd(arr):
    """
    This function returns the array with evens and odds segregated
    Args:
        arr: The list of elements
    Returns:
        The segregated list
    """
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] % 2 == 0:
            i += 1
        if arr[j] % 2 != 0:
            j -= 1
        if arr[i] % 2 != 0 and arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return arr
