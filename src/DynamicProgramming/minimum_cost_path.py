"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path
to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. The total cost of
a path to reach (m, n) is the sum of all the costs on that path (including both source and destination). You can only
traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j),
(i, j+1), and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

Example:
[1, 2, 3]
[4, 8, 2]
[1, 5, 3]
(0, 0) -> (2, 2)
The path with minimum cost is highlighted in the following figure. The path is (0, 0) –> (0, 1) –> (1, 2) –> (2, 2).
The cost of the path is 8 (1 + 2 + 2 + 3).
"""

from src.res.DynamicProgramming.minimum_cost_path import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    src_i, src_j = ip.src_i, ip.src_j
    dest_i, dest_j = ip.dest_i, ip.dest_j
    max_cost = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            max_cost = arr[i][j] if arr[i][j] > max_cost else max_cost
    result = minimum_cost_path_dp(arr, src_i, src_j, dest_i, dest_j, max_cost)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def minimum_cost_path(arr, src_i, src_j, dest_i, dest_j, max_cost):
    """
    This function calculates the minimum cost to traverse from source to destination recursively
    :param arr: The cost matrix
    :param src_i: source i index
    :param src_j: source j index
    :param dest_i: destination i index
    :param dest_j: destination j index
    :param max_cost: maximum cost in entire cost matrix
    :return: The minimum cost for the path
    """
    if src_i == len(arr[0]) or src_j == len(arr):
        return max_cost
    if src_i == dest_i and src_j == dest_j:
        return arr[src_i][src_j]
    cost_i_1_j_1 = minimum_cost_path(arr, src_i+1, src_j+1, dest_i, dest_j, max_cost)
    cost_i_1_j = minimum_cost_path(arr, src_i+1, src_j, dest_i, dest_j, max_cost)
    cost_i_j_1 = minimum_cost_path(arr, src_i, src_j+1, dest_i, dest_j, max_cost)
    return arr[src_i][src_j] + min(cost_i_1_j_1, min(cost_i_1_j, cost_i_j_1))


def minimum_cost_path_dp(arr, src_i, src_j, dest_i, dest_j, max_cost):
    """
    This function calculates the minimum cost to traverse from source to destination recursively
    :param arr: The cost matrix
    :param src_i: source i index
    :param src_j: source j index
    :param dest_i: destination i index
    :param dest_j: destination j index
    :param max_cost: maximum cost in entire cost matrix
    :return: The minimum cost for the path
    """
    dp = [[max for _ in range(len(arr[0])+1)] for _ in range(len(arr)+1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = max_cost
            else:
                dp[i][j] = arr[i-1][j-1]
    for i in range(src_i + 1, len(dp)):
        for j in range(src_j + 1, len(dp[0])):
            dp[i][j] = dp[i][j] + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))

    return dp[dest_i + 1][dest_j + 1]
