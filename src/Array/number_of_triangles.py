"""
Given an unsorted array of positive integers, find the number of triangles that can be formed with three different array elements as three sides of triangles. For a triangle to be possible from 3 values, the sum of any of the two values (or sides) must be greater than the third value (or third side).

Examples:

Input: arr= {4, 6, 3, 7}
Output: 3
Explanation: There are three triangles
possible {3, 4, 6}, {4, 6, 7} and {3, 6, 7}.
Note that {3, 4, 7} is not a possible triangle.

Input: arr= {10, 21, 22, 100, 101, 200, 300}.
Output: 6
Explanation: There can be 6 possible triangles:
{10, 21, 22}, {21, 100, 101}, {22, 100, 101},
{10, 100, 101}, {100, 101, 200} and {101, 200, 300}
"""
from src.res.Array.number_of_triangles import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(number_of_triangles(n))
        results.append(number_of_triangles_two_pointer(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def number_of_triangles(arr):
    """
    This function returns the count of triangles that can be made using elements of a list
    Args:
        arr: The list of elements
    Returns:
        The number of triangles possible
    """
    i, count = 0, 0
    visited = []
    while i < len(arr) - 2:
        j = i + 1
        while j < len(arr) - 1:
            k = j + 1
            while k < len(arr):
                res = [i, j, k]
                res.sort()
                if res not in visited\
                        and arr[i] + arr[j] > arr[k] \
                        and arr[i] + arr[k] > arr[j] \
                        and arr[j] + arr[k] > arr[i]:
                    count += 1
                    visited.append(res)
                k += 1
            j += 1
        i += 1
    return count


def number_of_triangles_two_pointer(arr):
    """
    This function returns the count of triangles that can be made using elements of a list using 2 Pointers approach
    Args:
        arr: The list of elements
    Returns:
        The number of triangles possible
    """
    arr.sort()
    arr_len = len(arr)
    i, count = arr_len - 1, 0
    while i > 1:
        j, k = 0, i - 1
        while j < k:
            if arr[j] + arr[k] > arr[i]:
                count += k - j
                k -= 1
            else:
                j += 1
        i -= 1
    return count
