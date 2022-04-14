"""
this program is implementation of Quick Sort
"""
from src.res.Practice.Sorting.quick_sort import input as ip, output as op


def quick_sort(arr, l, r):
    """
    This is the
    :param arr: The array to be considered
    :param l: The lower index for slicing
    :param r: The higher index for slicing
    :return:
    """
    if l >= r:
        return
    pivot = partition_algorithm(arr, l, r)
    quick_sort(arr, l, pivot - 1)
    quick_sort(arr, pivot + 1, r)
    return arr


def partition_algorithm(arr, l, r):
    """
    This is the implementation of the partition in Quick Sort Algorithm
    :param arr: The array to be considered
    :param l: The lower index for slicing
    :param r: The higher index for slicing
    :return: None
    """
    i = l - 1
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    if arr != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', arr)
