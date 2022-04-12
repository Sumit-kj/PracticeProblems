"""
Given an array arr[] of n non-negative integers representing the height of blocks. If width of each block is 1, compute
how much water can be trapped between the blocks during the rainy season.

Assuming the structure looks something like this for arr = [3, 0, 0, 2, 0, 4], the output is 10.

          |
| . . . . |
| . . | . |
| . . | . |
3 0 0 2 0 4

| shows column, and . shows water
"""
from src.res.Misc.trapping_rain_water import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    n = ip.n
    arr = ip.i_p
    result = trapping_rain_water(n, arr)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def trapping_rain_water(n, arr):
    """
    The function calculates the units of water trapped in structure with the column height as arr
    :param n: The number of elements
    :param arr: The list of height of each column
    :return: The units of water trapped in the structure
    """
    result = 0
    last_bound_index, next_bound_index, max_index, min_index = 0, 1, 0, 0
    for i in range(1, n):
        if arr[i] < arr[last_bound_index]:
            if arr[i] > arr[next_bound_index]:
                next_bound_index = i
        else:
            min_index = last_bound_index if arr[last_bound_index] < arr[i] else i
            water_units = 0
            for j in range(last_bound_index, i+1):

                water_units += arr[min_index] - arr[j]
            last_bound_index = i
        if next_bound_index > last_bound_index:
            min_index = last_bound_index if arr[last_bound_index] < arr[next_bound_index] else next_bound_index
            water_units = 0
            for j in range(last_bound_index, next_bound_index + 1):
                water_units += arr[min_index] - arr[j]
    return result
