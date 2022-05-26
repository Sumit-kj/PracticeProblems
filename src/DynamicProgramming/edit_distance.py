"""
Given two strings str1 and str2 and below operations that can be performed on str1. Find minimum number of edits
(operations) required to convert ‘str1’ into ‘str2’.
1. Insert
2. Remove
3. Replace

Example:
Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.
Replace 'n' with 'r', insert t, insert a
"""
from src.res.DynamicProgramming.edit_distance import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    str1 = arr[0]
    str2 = arr[1]
    result = edit_distance(str1, str2, len(str1), len(str2))
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def edit_distance(str1, str2, i1, i2):
    dp = [[-1 for _ in range(i2 + 1)] for _ in range(i1 + 1)]
    for i in range(i1 + 1):
        for j in range(i2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return i2 - dp[i1][i2]
