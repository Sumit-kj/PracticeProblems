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
from src.res.Stack.evaluate_reverse_polish_notation import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(evaluate_reverse_polish_notation(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def evaluate_reverse_polish_notation(tokens):
    """
    This function evaluates the reverse polish notation
    Args:
        tokens: The list of notations in reversed order
    Returns:
        The final value of expressions when solved
    """
    values = []
    top = -1
    for t in tokens:
        if t.isnumeric() or t[1:].isnumeric():
            if t[0] == '-' and len(t) != 1:
                t = int(t[1:]) * -1
            values.append(int(t))
            top += 1
        else:
            if top >= 1:
                val = 0
                if t == '+':
                    val = values[top - 1] + values[top]
                elif t == '-':
                    val = values[top - 1] - values[top]
                elif t == '*':
                    val = values[top - 1] * values[top]
                elif t == '/':
                    val = values[top - 1] // values[top]
                    if val < 0 and float(values[top - 1] // values[top]) != values[top - 1] / values[top]:
                        val += 1
                top -= 1
                values = values[:-2]
                values.append(val)
    return values[top]
