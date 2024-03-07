"""
Given an array of integers, our task is to write a program that efficiently finds the second-largest element present in
the array.

Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second-largest element is 34.
Explanation: The largest element of the array is 35 and the second-largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second-largest element is 5.
Explanation: The largest element of the array is 10 and the second-largest element is 5

Input: arr[] = {10, 10, 10}
Output: The second-largest does not exist.
Explanation: Largest element of the array is 10 there is no second-largest element
"""
from src.res.Array.second_largest_element import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(second_largest_element(n))
        results.append(second_largest_element_sort(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def second_largest_element(arr):
    """
    This function returns the 2nd largest element from array
    Params:
        arr: The list of elements
    Returns:
        The 2nd Largest element in the list
    """
    if len(set(arr)) == 1:
        return None
    if arr[0] > arr[1]:
        l_1, l_2 = arr[0], arr[1]
    else:
        l_1, l_2 = arr[1], arr[0]
    ind = 2
    while ind < len(arr):
        if arr[ind] > l_1:
            l_2 = l_1
            l_1 = arr[ind]
        elif arr[ind] > l_2 and arr[ind] != l_1:
            l_2 = arr[ind]
        ind += 1
    return l_2


def second_largest_element_sort(arr):
    """
    This function returns the 2nd largest element from array
    Params:
        arr: The list of elements
    Returns:
        The 2nd Largest element in the list
    """
    arr.sort()
    res = list(set(arr))
    res.sort()
    return res[-2] if len(res) > 1 else None
