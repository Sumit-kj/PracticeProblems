"""
Given an array arr[] of N elements, sort the array according to the following relations:

arr[i] >= arr[i – 1], if i is even, ∀ 1 <= i < N
arr[i] <= arr[i – 1], if i is odd, ∀ 1 <= i < N
Print the resultant array.

Examples:
Input: N = 4, arr[] = {1, 2, 2, 1}
Output: 2 1 2 1
Explanation:
For i = 1, arr[1] <= arr[0]. So, 1 <= 2.
For i = 2, arr[2] >= arr[1]. So, 2 >= 1.
For i = 3, arr[3] <= arr[2]. So, 1 <= 2.
Input: arr[] = {1, 3, 2}
Output: 3 1 2
Explanation:

For i = 1, arr[1] <= arr[0]. So, 1 <= 3.
For i = 2, arr[2] >= arr[1]. So, 2 >= 1.
"""
from src.res.Array.even_position_greater_than_odd import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(even_position_greater_than_odd(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def even_position_greater_than_odd(arr):
    """
    This function rearranges the array such that elements at even places are larger than at previous odd place
    Approach: Sort the array, pick alternate from last and first of the list and make a new list
    Args:
        arr: The list of elements
    Returns:
        The rearranged list
    """
    arr.sort()
    arr_final = []
    i, j = 0, len(arr) - 1
    while i < j:
        arr_final.append(arr[j])
        arr_final.append(arr[i])
        i += 1
        j -= 1
    if i == j:
        arr_final.append(arr[i])
    return arr_final


def even_position_greater_than_odd_linear(arr):
    """
    This function rearranges the array such that elements at even places are larger than at previous odd place
    Approach: Swap elements that don't satisfy the condition in steps of 2 elements
    Args:
        arr: The list of elements
    Returns:
        The rearranged list
    """
    arr_len = len(arr)
    i = 0
    while i < arr_len - 1:
        # Compare first and second element, check for adjacent next and swap if smaller in steps of 2
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # Compare next and next to next element to check if the odd-even grater condition is met, else swap
        if i < arr_len - 2 and arr[i+1] > arr[i+2]:
            arr[i+1], arr[i+2] = arr[i+2], arr[i+1]
        i += 2
    return arr