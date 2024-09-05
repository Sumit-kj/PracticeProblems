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
        # results.append(search_sorted_2d_array(n[0], n[1]))
        results.append(search_sorted_2d_array_binary(n[0], n[1]))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def search_sorted_2d_array(matrix, target):
    """
    This function implements search in 2d Array.
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


def search_sorted_2d_array_binary(matrix, target):
    """
    This function implements binary search in 2d Array.
    Args:
        matrix: The 2D Array
        target: The target to be found
    Returns: True if target is present in the 2D array, otherwise False
    """
    r_l, r_h, c_l, c_h = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    r_mid, c_mid = (len(matrix) - 1) //2, (len(matrix[0]) - 1) //2
    while r_l <= r_h:
        r_mid = (r_l + r_h) // 2
        if matrix[r_mid][0] <= target <= matrix[r_mid][-1]:
            break
        elif matrix[r_mid][0] > target:
            r_h = r_mid - 1
        elif matrix[r_mid][-1] < target:
            r_l = r_mid + 1
    while c_l <= c_h:
        c_mid = (c_l + c_h) // 2
        if matrix[r_mid][c_mid] == target:
            return True
        elif matrix[r_mid][c_mid] > target:
            c_h = c_mid - 1
        elif matrix[r_mid][c_mid] < target:
            c_l = c_mid + 1
    return False
