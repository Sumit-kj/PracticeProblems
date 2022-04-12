"""
Consider an array of n integers, A = {a1, a2, ..., an}. Find and print the total number of (i, j) pairs such that
ai x aj <= max(ai, ai+1, ..., aj)where i<j.
"""
import os
from src.res.Misc.array_pair import output as op


def array_pair_basic(arr):
    """
    This function gives the number of pair of elements of an array
    :param arr: the given array
    :return: the number of pairs
    """
    result = 0
    i = 0
    n = len(arr)
    while i < n-1:
        j = i + 1
        while j < n:
            max_a = max(arr[i:j+1])
            if arr[i] * arr[j] <= max_a:
                result += 1
            j += 1
        i += 1
    return result


def array_pair(arr, n):
    """
    This function gives the number of pair of elements of an array
    :param n: length of array
    :param arr: the array
    :return: count of pairs
    """
    count = 0
    i = 0
    while i < n-1:
        j = i + 1
        max_a = arr[i]
        while j < n:
            if arr[j] > max_a:
                max_a = arr[j]
            if arr[i] * arr[j] <= max_a:
                count += 1
            j += 1
        i += 1
    return count


def solve():
    """
    The solution of the program
    :return: None
    """
    script_dir = os.path.dirname(__file__)
    rel_path = "../res/Misc/array_pair/input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        n = int(f.readline().strip())

        # arr = []

        # for _ in range(n):
        arr = list(map(int, f.readline().rstrip().split()))

        result = array_pair(arr, n)
        print(result)

        if result != op.o_p:
            print()
            print('Wrong answer')
            print('Expected output:', op.o_p)
            print('Your output:', result)
