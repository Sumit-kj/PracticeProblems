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
from src.res.Stack.baseball_game import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(baseball_game(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def baseball_game(operations):
    """
    This function returns the final score after performing a set of instructions
    Args:
        operations: The list opf operations to be done
    Returns:
        The final score of the baseball game
    """
    scores = []
    top = -1
    for o in operations:
        if o.isnumeric() or o[1:].isnumeric():
            if o[0] == -1:
                o = int(o[1:]) * -1
            scores.append(int(o))
            top += 1
        elif o == '+':
            if top >= 1:
                scores.append(scores[top] + scores[top - 1])
                top += 1
        elif o == 'D':
            scores.append(scores[top] * 2)
            top += 1
        elif o == 'C':
            if top >= 0:
                scores = scores[:-1]
                top -= 1
    final_score = 0
    for i in scores:
        final_score += i
    return final_score
