"""
Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number
of platforms required for the railway station so that no train waits.
We are given two arrays that represent the arrival and departure times of trains that stop.

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)

Input: arr[] = {9:00, 9:40}
dep[] = {9:10, 12:00}
Output: 1
Explanation: Only one platform is needed.
"""
from src.res.Greedy.minimum_number_of_platforms import input as ip, output as op
import time


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = convert_str_to_time(ip.arr)
    dep = convert_str_to_time(ip.dep)
    result = min_number_of_platforms(arr, dep)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def convert_str_to_time(time_list):
    """
    Converts String to Time type
    :param time_list: list of time to be converted form string
    :return: None
    """
    for i, t in enumerate(time_list):
        converted_time = time.strptime(t, "%H:%M")
        time_list[i] = converted_time
    return time_list


def min_number_of_platforms(arr, dep):
    """
    Calculates the minimum number of platforms required for a station
    :param arr: list of arrival time
    :param dep: list of departure time
    :return: the number of platforms required
    """
    result = 0
    concurrent_count = [1 for _ in range(len(arr) - 1)]
    for i in range(len(arr) - 1):
        concurrent_trains(arr, dep, i, dep[i], concurrent_count)
    for c in concurrent_count:
        if c > result:
            result = c
    return result


def concurrent_trains(arr, dep, i, min_dep, concurrent_count):
    """
    To check concurrency of trains for ith train
    :param arr: the arrival time list
    :param dep: the departure time for first train
    :param i: the iteration
    :param min_dep: the minimum departure to be considered for all trains to be concurrent, i.e. the arrival should be
            before this time
    :param concurrent_count: the count of concurrency at that time period
    :return: none
    """
    if i == len(arr) - 1 or arr[i+1] > min_dep:
        return
    concurrent_count[i] += 1
    min_dep = dep[i+1] if min_dep > dep[i+1] else min_dep
    concurrent_trains(arr, dep, i+1, min_dep, concurrent_count)

