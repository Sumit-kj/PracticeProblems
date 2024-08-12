"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from src.res.String.largest_substring_non_repeating import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(largest_substring_non_repeating(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def largest_substring_non_repeating(s):
    """
    This function returns the length of the largest substring of the string
    Params:
        s: The string
    Return:
        The length of largest substring without repeating characters
    """
    index_char = {}
    visit_char = {}
    curr_str = ''
    max_len = 0
    for ind, c in enumerate(s):
        # wtf did I just write, lmao
        if c not in index_char.keys() or index_char[c] == -1:
            index_char[c] = ind
            visit_char[c] = True
            curr_str += c
        else:
            if len(curr_str) > max_len:
                max_len = len(curr_str)
            curr_str = curr_str[index_char[c] + 1:] + c
            index_char[c] = ind
            for k in index_char.keys():
                if index_char[k] < ind:
                    index_char[k] = -1
                    visit_char[c] = False
            visit_char[c] = True

        if len(curr_str) > max_len:
            max_len = len(curr_str)
    return max_len

