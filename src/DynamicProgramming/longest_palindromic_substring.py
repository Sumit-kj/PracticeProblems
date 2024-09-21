"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""
from src.res.DynamicProgramming.longest_palindromic_substring import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    i_p = ip.i_p
    results = []
    for s in i_p:
        results.append(longest_palindromic_substring(s))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def longest_palindromic_substring(s):
    """
    This function returns the longest palindromic substring for a string
    :param s: The string
    :return: longest palindromic substring
    """
    s_rev = ''
    for c in s:
        s_rev = c + s_rev
    m = n = len(s) + 1
    inter = []
    for _ in range(m):
        i = []
        for _ in range(n):
            i.append(0)
        inter.append(i)

    i = 1
    while i < m:
        j = 1
        while j < n:
            if s[i - 1] == s_rev[j - 1]:
                inter[i][j] = inter[i - 1][j - 1] + 1
            else:
                inter[i][j] = max(inter[i - 1][j], inter[i][j - 1])
            j += 1
        i += 1

    res = ''
    i = j = m
    while i > 0:
        while j > 0:
            if inter[i][j] == inter[i][j - 1]:
                continue
            else:
                res += s[i - 1]
            j -= 1
        i -= 1
    return inter[m - 1][n - 1]
