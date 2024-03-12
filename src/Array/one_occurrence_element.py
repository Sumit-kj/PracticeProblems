"""
Given an array of integers. All numbers occur twice except one number which occurs once. Find the number in O(n) time & constant extra space.

Example :

Input:  arr[] = {2, 3, 5, 4, 5, 3, 4}
Output: 2
"""
from src.res.Array.one_occurrence_element import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(one_occurrence_element(n))
        results.append(one_occurrence_element_xor(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def one_occurrence_element(arr):
    """
    This function returns the element that is present only once in the list
    Args:
        arr: The list of elements
    Returns:
        The element that is present once
    """
    element_count = {}
    for i in arr:
        if i in element_count:
            element_count[i] += 1
        else:
            element_count[i] = 1
    for i in element_count:
        if element_count[i] == 1:
            return i
    return -1


def one_occurrence_element_xor(arr):
    """
    This function returns the element that is present only once in the list using XOR
    Args:
        arr: The list of elements
    Returns:
        The element that is present once
    """
    xor_value = arr[0]
    for i in range(1, len(arr)):
        xor_value = xor_value ^ arr[i]
    return xor_value
