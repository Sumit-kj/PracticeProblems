"""
Given an array Arr[] of size N, print all the subsets of the array.

Subset: A subset of an array is a tuple that can be obtained from the array by removing some (possibly all) elements of
it

Input: N = 3, Arr = [1, 2, 3]
Output: {}
               {1}
               {1, 2}
               {1, 2, 3}
               {1, 3}
               {2}
               {2, 3}
               {3}
Explanation: These are all the subsets that can be formed from the given array, it can be proven that no other subset
exists other than the given output.


Input: N = 2, Arr = [2, 4]
Output: {}
               {2}
               {2, 4}
               {4}
Explanation: These are all the subsets that can be formed from the given array, it can be proven that no other subset
exists other than the given output.
"""
from src.res.Backtracking.all_possible_subsets import input as ip, output as op
import validator


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(all_possible_subsets(n))
    print(results)

    if not validator.are_two_arrays_same(op.o_p, results):
        print()
        print('Wrong answer')
        print('Expected output pattern:', op.o_p)
        print('Your output:', results)


def all_possible_subsets(arr):
    res = []
    visited = [0 for _ in arr]
    index = 0
    subset_recur(arr, visited, res, index)
    return res


def subset_recur(arr, visited, res, index):
    """
    This function recursively traverses the whole array, considering one element at a time, finding all possible subsets
    :param arr: The array for which all possible subsets are to bbe found
    :param visited: The intermediate array to store current possible subset
    :param res: The resultant array
    :param index: The index of element into consideration
    """
    if index == len(arr):
        inter = []
        for i in range(len(visited)):
            if visited[i] == 1:
                inter.append(arr[i])
        res.append(inter)
        return
    visited[index] = 0
    subset_recur(arr, visited, res, index + 1)
    visited[index] = 1
    subset_recur(arr, visited, res, index + 1)
