"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""
from src.res.Array.search_sorted_2d_array import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(search_sorted_2d_array(n[0], n[1]))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def search_sorted_2d_array(matrix, target):
    """
    This function implements binary search in 2d Array.
    Args:
        matrix: The 2D Array
        target: The target to be found
    Returns: True if target is present in the 2D array, otherwise False
    """
    i, j = 0, 0
    while i < len(matrix) and matrix[i][0] <= target:
        i += 1
    i -= 1
    while j < len(matrix[i]) and matrix[i][j] < target:
        j += 1
    if i < len(matrix) and j < len(matrix[i]) and matrix[i][j] == target:
        return True
    return False
