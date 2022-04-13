"""
this program is implementation of Merge Sort
"""
from src.res.Practice.Sorting.merge_sort import input as ip, output as op


def merge_sort(arr, l, r):
    """
    This is the recursive implementation of Merge Sort Algorithm
    :param arr: The array
    :param l: The left bound Index
    :param r: The right bound Index
    :return: None
    """
    if l >= r:
        return
    m = (r + l)//2
    merge_sort(arr, l, m)
    merge_sort(arr, m + 1, r)
    merge_algorithm(arr, l, m, r)


def merge_algorithm(arr, l, m, r):
    """
    This is the Merge implementation of the Merge Sort Algorithm
    :param arr: The array to be considered
    :param l: The lower index for slicing
    :param m: The middle index for slicing
    :param r: The higher index for slicing
    :return: None
    """
    i, j = l, m + 1
    res = []
    size = r - l + 1
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            res.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            res.append(arr[j])
            j += 1
    if i > m:
        res.extend(arr[j: r + 1])
    else:
        res.extend(arr[i: m + 1])
    i = 0
    while i < size:
        arr[l + i] = res[i]
        i += 1


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

    if arr != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', arr)
