"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from src.res.Array.valid_sudoku import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(valid_sudoku(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def valid_sudoku(board):
    """
    This function checks if the Sudoku board is valid or not
    """
    fixed_count = 9
    fixed_root_count = 3
    for i in range(fixed_count):
        key_map = get_empty_key_map()
        for j in range(fixed_count):
            cell = board[i][j]
            if cell != '.':
                if key_map[cell] != 0:
                    return False
                key_map[cell] += 1
        for k in key_map.keys():
            if key_map[k] != 0 and key_map[k] != 1:
                return False

    for i in range(fixed_count):
        key_map = get_empty_key_map()
        for j in range(fixed_count):
            cell = board[j][i]
            if cell != '.':
                if key_map[cell] != 0:
                    return False
                key_map[cell] += 1
        for k in key_map.keys():
            if key_map[k] != 0 and key_map[k] != 1:
                return False

    for i in range(fixed_root_count):
        for j in range(fixed_root_count):
            key_map = get_empty_key_map()
            for i_1 in range(3*i, 3*(i + 1)):
                for j_1 in range(3*j, 3*(j + 1)):
                    cell = board[i_1][j_1]
                    if cell != '.':
                        if key_map[cell] != 0:
                            return False
                        key_map[cell] += 1
        for k in key_map.keys():
                if key_map[k] != 0 and key_map[k] != 1:
                    return False
    return True


def get_empty_key_map():
    return {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
    }