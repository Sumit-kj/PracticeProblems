"""
An array contains both positive and negative numbers in random order. Rearrange the array elements so that positive and
negative numbers are placed alternatively. A number of positive and negative numbers need not be equal. If there are
more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the
end of the array.

Example:

Input: [-1, 2, -3, 4, 5, 6, -7, 8, 9]
Output:[9, -7, 8, -3, 5, -1, 2, 4, 6]

Input: [-1, 3, -2, -4, 7, -5]
Output:[7, -2, 3, -5, -1, -4]
"""
from src.res.Array.rearrange_positive_negative import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(rearrange_positive_negative(n))
        results.append(rearrange_positive_negative_optimal(n))
    print(results)

    output_sum = 0
    for i in range(len(arr)):
        output_sum += op.validate_output(results[i])
    if output_sum != len(arr):
        print()
        print('Wrong answer')
        print('Expected output pattern:', op.o_p)
        print('Your output:', results)


def rearrange_positive_negative(arr):
    """
    This function returns positive and negative elements at alternates
    Args:
        arr: The list of elements
    Returns:
        The rearranged list
    """
    n = len(arr)
    arr.sort()
    rearranged = []
    i = 0
    while i < n//2:
        rearranged.append(arr[n - 1 - i])
        rearranged.append(arr[i])
        i += 1
    if i == n//2:
        rearranged.append(arr[i])
    return rearranged


def rearrange_positive_negative_optimal(arr):
    """
    This function returns positive and negative elements at alternates
    Args:
        arr: The list of elements
    Returns:
        The rearranged list
    """
    n = len(arr)
    i, j = 0, 0
    pos_index, neg_index, is_done = 0, 1, False
    while not is_done:
        while i < n/2:
            # What I'm trying to do is loop for n/2, and check for 2i, and 2i + 1 if even and odd respectively,
            if arr[2 * i] > 0:
                i += 1
                continue
            else:
                pos_index = 2 * i
                i += 1
                break
        while j < n/2:
            if arr[2 * j + 1] < 0:
                j += 1
                continue
            else:
                neg_index = 2 * j + 1
                j += 1
                break
        if arr[pos_index] < 0 < arr[neg_index]:
            arr[pos_index], arr[neg_index] = arr[neg_index], arr[pos_index]
        if i >= n//2 or j >= n//2:
            is_done = True
    return arr























