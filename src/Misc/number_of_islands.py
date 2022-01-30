"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below
matrix contains 5 islands

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}}
Output : 5
"""
from src.res.number_of_islands import input as ip
from src.res.number_of_islands import output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    result = number_of_islands(arr)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def number_of_islands(arr):
    """
    This function calculates the total number of islands found in the graph
    :param arr: The array for graph
    :return: number of islands from the graph
    """
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                result += 1
                traverse_dfs(arr, i, j)
    return result


def traverse_dfs(graph, i, j):
    """
    To Traverse Depth First Search for a graph
    :param graph: 2D array representation of a graph
    :param i: row of current consideration
    :param j: column of current consideration
    :return: None
    """
    if i < 0 or j < 0 or i >= len(graph) or j >= len(graph[0]) or graph[i][j] != 1:
        return
    graph[i][j] = -1
    traverse_dfs(graph, i-1, j-1)
    traverse_dfs(graph, i-1, j)
    traverse_dfs(graph, i-1, j+1)
    traverse_dfs(graph, i, j)
    traverse_dfs(graph, i, j)
    traverse_dfs(graph, i+1, j-1)
    traverse_dfs(graph, i+1, j)
    traverse_dfs(graph, i+1, j+1)
