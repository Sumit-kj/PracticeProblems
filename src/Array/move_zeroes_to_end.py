"""
Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the
given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order
of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

Example:

Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
"""
from src.res.Array.move_zeroes_to_end import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(move_zeroes_to_end(n))
        results.append(move_zeroes_to_end_linear(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def move_zeroes_to_end(arr):
    """
    This function moves all the non-zero elements, in front of the array
    Approach: Move elements when encountered a zero using 2 for loops
    Args:
        arr: The list of elements
    Returns:
        List with zeroes moved to the end
    """
    arr_len = len(arr)
    i = 0
    while i < arr_len - 1:
        if arr[i] != 0:
            i += 1
            continue
        j = i + 1
        while j < arr_len:
            if arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                break
            j += 1
        i += 1
    return arr


def move_zeroes_to_end_linear(arr):
    """
    This function moves all the non-zero elements, in front of the array
    Approach: Linear Traversal of list
    Args:
        arr: The list of elements
    Returns:
        List with zeroes moved to the end
    """
    arr_len = len(arr)
    top = 0
    for i in range(arr_len):
        if arr[i] != 0:
            arr[top] = arr[i]
            top += 1
    while top < arr_len:
        arr[top] = 0
        top += 1
    return arr