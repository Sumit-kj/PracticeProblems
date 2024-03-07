"""
Given an array with all distinct elements, find the largest three elements.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1).

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23

Input: arr[] = { 6, 8, 1, 9, 2, 1, 10, 10}
Output: 10, 10, 9
"""
from src.res.Array.largest_three_distinct_elements import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(largest_three_distinct_elements(n))
        results.append(largest_three_distinct_elements_sort(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def largest_three_distinct_elements(arr):
    """
    This function returns the 3 largest elements from a list
    Params:
        arr: The array of elements
    Return:
        The listy of 3 largest elements
    """
    l_1, l_2, l_3 = arr[0], arr[0], arr[0]
    for i in arr:
        if i > l_1:
            l_3 = l_2
            l_2 = l_1
            l_1 = i
        elif i > l_2:
            l_3 = l_2
            l_2 = i
        elif i > l_3:
            l_3 = i
    return [l_1, l_2, l_3]


def largest_three_distinct_elements_sort(arr):
    """
    This function returns the 3 largest elements from a list using sort
    Params:
        arr: The array of elements
    Return:
        The listy of 3 largest elements
    """
    arr.sort()
    return [arr[-1], arr[-2], arr[-3]]
