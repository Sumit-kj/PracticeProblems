"""
Example 1 : Consider the following 3 activities sorted
by finish time.
     start[]  =  {10, 12, 20};
     finish[] =  {20, 25, 30};
A person can perform at most two activities. The
maximum set of activities that can be executed
is {0, 2} [ These are indexes in start[] and
finish[] ]

Example 2 : Consider the following 6 activities
sorted by finish time.
     start[]  =  {1, 3, 0, 5, 8, 5};
     finish[] =  {2, 4, 6, 7, 9, 9};
A person can perform at most four activities. The
maximum set of activities that can be executed
is {0, 1, 3, 4} [ These are indexes in start[] and
finish[] ]
"""
from src.res.Greedy.activity_selection import output as op, input as ip


def solve():
    """
    The solution of the program
    :return: None
    """
    s = ip.s
    f = ip.f
    result = max_activity(s, f)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def max_activity(s, f):
    """
    This function gives the list of maximum problems that can be solved
    :param s: list of starting time
    :param f: list of finishing time
    :return: the list of order of activities
    """
    result = [0]
    i = 0
    j = i + 1
    while j in range(len(s)):
        if f[i] < s[j] and j not in result:
            result.append(j)
            i = j
            continue
        j += 1
    return result
