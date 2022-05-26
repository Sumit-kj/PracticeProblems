"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""
from src.res.DynamicProgramming.longest_common_subsequence import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    str1 = arr[0]
    str2 = arr[1]
    # result = longest_common_subsequence(str1, str2, len(str1), len(str2))
    result = longest_common_subsequence_dp(str1, str2, len(str1), len(str2))
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def longest_common_subsequence(str1, str2, i1, i2):
    """
    This function finds the length of the longest common subsequence recursively
    :param str1: The first string
    :param str2: The second string
    :param i1: The first string's index
    :param i2: The second string's index
    :return: The length of the longest common subsequence
    """
    if i1 == 0 or i2 == 0:
        return 0
    if str1[i1 - 1] == str2[i2 - 1]:
        return 1 + longest_common_subsequence(str1, str2, i1 - 1, i2 - 1)
    return max(longest_common_subsequence(str1, str2, i1 - 1, i2),
               longest_common_subsequence(str1, str2, i1, i2 - 1))


def longest_common_subsequence_dp(str1, str2, i1, i2):
    """
    This function finds the length of the longest common subsequence
    :param str1: The first string
    :param str2: The second string
    :param i1: The first string's index
    :param i2: The second string's index
    :return: The length of the longest common subsequence
    """

    dp = [[-1 for _ in range(i1 + 1)] for _ in range(i2 + 1)]
    for i in range(i1 + 1):
        for j in range(i2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[i1][i2]



