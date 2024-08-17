"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty
record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is
one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
"""
from src.res.Stack.valid_parentheses import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(valid_parentheses(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def valid_parentheses(s):
    """
    This function returns true if the sequence of parentheses is valid, otherwise false
    Args:
        s: The string containing sequence of parentheses
    Returns:
        True, if the sequence is valid, otherwise false
    """
    paren = []
    paren_match_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    top = -1
    for p in s:
        if top == -1:
            paren.append(p)
            top += 1
        else:
            if p in paren_match_map.keys() and paren[top] == paren_match_map[p]:
                paren = paren[:-1]
                top -= 1
            else:
                paren.append(p)
                top += 1
    return top == -1
