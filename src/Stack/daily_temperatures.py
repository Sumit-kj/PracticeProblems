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
from src.res.Stack.daily_temperatures import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(daily_temperatures(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def daily_temperatures(temperatures):
    """
    This function returns the number of days before which temperature is higher than that day
    Args:
        temperatures: the list of temperatures
    Returns:
        The number of days before which the temperature is higher than that respective day
    """
    temp = []
    results = [0] * len(temperatures)
    top = -1
    for index, t in enumerate(temperatures):
        if top == -1:
            temp.append((t, index))
            top += 1
        else:
            if t <= temp[top][0]:
                temp.append((t, index))
                top += 1
            else:
                while top > -1 and t > temp[top][0]:
                    results[temp[top][1]] = index - temp[top][1]
                    temp = temp[:-1]
                    top -= 1
                temp.append((t, index))
                top += 1
    return results
