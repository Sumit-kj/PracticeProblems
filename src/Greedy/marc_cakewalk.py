"""
Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to
expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least
2^j x c miles to maintain. Find the minimum number of miles Marc has to walk to compensate for the cupcakes
"""
from src.res.Greedy.marc_cakewalk import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.arr
    result = marcs_cakewalk(arr)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def marcs_cakewalk(calorie):
    """
    To calculate the number of miles Marc has to walk
    :param calorie: the calorie count for each cupcake
    :return: to total number of miles he has to walk
    """
    miles = 0
    calorie.sort(reverse=True)
    for i, c in enumerate(calorie):
        miles += (c * (2 ** i))
    return miles
