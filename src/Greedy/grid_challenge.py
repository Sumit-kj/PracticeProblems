"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending.
Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they
are not.

grid = ['abc', 'ade', 'efg']
output - YES
"""
from src.res.Greedy.grid_challenge import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    n = ip.n
    grid = ip.grid
    result = grid_challenge(grid, n)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def grid_challenge(grid, n):
    """
    To see if all the elements in each column are alphabetically sorted
    :param grid: the list of strings
    :param n: the number of rows or columns
    :return: YES if they're sorted, else NO
    """
    char_list = []
    for i, row in enumerate(grid):
        row_char = []
        for c in row:
            row_char.append(c)
        row_char.sort()
        char_list.append(row_char)

    print(char_list)
    for j in range(len(grid[0])):
        for k in range(n-1):
            if char_list[k][j] > char_list[k+1][j]:
                return 'NO'
    return 'YES'
