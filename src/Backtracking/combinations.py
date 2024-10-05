"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""
from src.res.Backtracking.combinations import input as ip, output as op
import validator


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(combinations(n[0], n[1]))
    print(results)

    if not validator.are_two_arrays_same(op.o_p, results):
        print()
        print('Wrong answer')
        print('Expected output pattern:', op.o_p)
        print('Your output:', results)


def combinations(n, k):
    """
    This function returns all the possible combinations of k elements out of first n natural elements
    :param n: The total number of natural elements
    :param k: The number of elements to be selected
    :return: All possible combinations of k elements from first n natural numbers
    """
    universe = [i for i in range(1, n + 1)]
    result = []
    visited = [0 for i in range(n)]
    count, index = 0, 0
    combination_recur(universe, visited, index, count, k, result)
    return result


def combination_recur(universe, visited, index, count, k, result):
    """
    This function recursively iterates through all possible combinations and adds plausible ones to result
    :param universe: The universe set from which elements are to be selected
    :param visited: The visited array that checks which elements are considered and which aren't
    :param index: The index for the element to be considered
    :param count: The count of elements that are considered
    :param k: The number of elements to be selected out of universe set
    :param result: The result array with all possible combinations
    """
    if count == k:
        inter = []
        for i in range(len(visited)):
            if visited[i] == 1:
                inter.append(universe[i])
        result.append(inter)
        return
    if index == len(universe):
        return
    visited[index] = 1
    combination_recur(universe, visited, index + 1, count + 1, k, result)
    visited[index] = 0
    combination_recur(universe, visited, index + 1, count, k, result)
