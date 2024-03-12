"""
Write a program to print all the LEADERS in the array. An element is a leader if it is greater than all the elements to its right side. And the rightmost element is always a leader.

For example:

Input: arr[] = {16, 17, 4, 3, 5, 2},
Output: 17, 5, 2

Input: arr[] = {1, 2, 3, 4, 5, 2},
Output: 5, 2
"""
from src.res.Array.leader_in_a_list import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        # results.append(leader_in_a_list(n))
        results.append(leader_in_a_list_linear(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def leader_in_a_list(arr):
    """
    This function return the leaders of a list
    Args:
        arr: The list of elements
    Returns:
        The list of leaders from the list
    """
    leaders = []
    arr_len = len(arr)
    for i in range(arr_len):
        if i == arr_len - 1:
            leaders.append(arr[i])
            break
        j = i + 1
        is_max = True
        while j < arr_len:
            if arr[j] > arr[i]:
                is_max = False
            j += 1
        if j == arr_len and is_max:
            leaders.append(arr[i])
    return leaders


def leader_in_a_list_linear(arr):
    """
    This function return the leaders of a list in a linear time complexity
    Args:
        arr: The list of elements
    Returns:
        The list of leaders from the list
    """
    arr_len = len(arr)
    i = arr_len - 2
    max_elem = arr[i + 1]
    leaders = []
    max_list = [max_elem] * arr_len
    while i > -1:
        if arr[i] > max_elem:
            max_elem = arr[i]
        max_list[i] = max_elem
        i -= 1
    for i in range(arr_len):
        if arr[i] == max_list[i]:
            leaders.append(arr[i])
    return leaders

