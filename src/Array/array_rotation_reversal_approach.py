"""
Given an array arr[] of size N, the task is to rotate the array by d position to the left.

Examples:

Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3, 4, 5, 6, 7, 1, 2
Explanation: If the array is rotated by 1 position to the left,
it becomes {2, 3, 4, 5, 6, 7, 1}.
When it is rotated further by 1 position,
it becomes: {3, 4, 5, 6, 7, 1, 2}

Input: arr[] = {1, 6, 7, 8}, d = 3
Output: 8, 1, 6, 7
"""
from src.res.Array.array_rotation_reversal_approach import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(even_position_greater_than_odd(n[0], n[1]))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def even_position_greater_than_odd(arr, d):
    """
    This function rotates an array by d positions using reversal approach
    Args:
        arr: The list of elements
        d: the number of positions to rotate by
    Returns:
        The rotated array
    """
    arr_1 = reverse_list(arr[:d], 0, len(arr[:d]))
    arr_2 = reverse_list((arr[d:]), 0, len(arr[d:]))
    arr_1.extend(arr_2)
    return reverse_list(arr_1, 0, len(arr_1))


def reverse_list(arr, start, end):
    """
    This functions reverses the array between the start and end indices
    Args:
        arr: The array of elements
        start: The start index
        end: The end index
    Returns:
        The rotated array between the two indices
    """
    # Excluding the last index
    end -= 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
