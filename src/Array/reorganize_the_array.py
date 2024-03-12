"""
Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If the
element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is
not present, display -1 at that place.

Examples:

Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19]
"""
from src.res.Array.reorganize_the_array import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(reorganize_the_array(n))
        results.append(reorganize_the_array_linear(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def reorganize_the_array(arr):
    """
    This function reorganizes the array such that arr[i] = i, -1 otherwise
    Args:
        arr: The list of elements
    Returns:
        The resultant array
    """
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == i:
            i += 1
            continue
        else:
            j = 0
            while j < n:
                if arr[j] == i:
                    arr[j], arr[i] = arr[i], arr[j]
                    break
                j += 1
        i += 1
    return arr


def reorganize_the_array_linear(arr):
    """
        This function reorganizes the array such that arr[i] = i, -1 otherwise in linear time complexity
        Args:
            arr: The list of elements
        Returns:
            The resultant array
        """
    n = len(arr)
    elements = {}
    for i in range(n):
        elements[i] = -1
    i = 0
    while i < n:
        if arr[i] != -1:
            elements[arr[i]] = arr[i]
        i += 1
    for i in range(n):
        arr[i] = elements[i]
    return arr
