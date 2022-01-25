"""
The median of a set of integers is the midpoint value of the data set for which an equal number of integers are less
than and greater than the value. To find the median, you must first sort your set of integers in non-decreasing order,
then:

If your set contains an odd number of elements, the median is the middle element of the sorted sample. In the sorted
set {1,2,3}, 2 is the median.
If your set contains an even number of elements, the median is the average of the two middle elements of the sorted
sample. In the sorted set {1,2,3,4}, ()2+3/2 = 2.5 is the median.
Given an input stream of  integers, perform the following task for each ith integer:

Add the ith integer to a running list of integers.
Find the median of the updated list (i.e., for the first element through the ithj element).
Print the updated median on a new line. The printed value must be a double-precision number scaled to 1 decimal place
(i.e., 12.3 format).
"""
import os
from src.res.running_median import output as op


def solution(a):
    """
    To find the running median of the array
    :param a: the array to which median we've to find
    :return: list of running median
    """
    sorted_a = []
    sorted_a_1 = []
    sorted_a_2 = []
    res = []
    res_1 = []
    res_2 = []
    med_flag = True
    for e in a:
        sorted_a.append(float(e))
        sorted_a.sort()
        med = calculate_median(med_flag, sorted_a)
        res.append(med)

        ind = get_insert_index(sorted_a_1, float(e))
        sorted_a_1.insert(ind, float(e))
        med = calculate_median(med_flag, sorted_a_1)
        res_1.append(med)

        ind_1 = get_insert_index_binary(sorted_a_1, float(e))
        sorted_a_2.insert(ind_1, float(e))
        med = calculate_median(med_flag, sorted_a_2)
        res_2.append(med)

        med_flag = not med_flag
    return res, res_1, res_2


def calculate_median(med_flag, sorted_a):
    """
    To calculate median of a given array
    :param med_flag: the flag which says if number of elements is even or odd
    :param sorted_a: the sorted array
    :return: the median of the array
    """
    med = -1
    if med_flag:
        med = sorted_a[len(sorted_a) // 2]
    else:
        med = (sorted_a[len(sorted_a) // 2] + sorted_a[len(sorted_a) // 2 - 1]) / 2
    return med


def get_insert_index(a, e):
    """
    To gte the index where we can insert element in a sorted array
    :param a: sorted array
    :param e: element
    :return: index to insert the value
    """
    ind = -1
    for i in range(len(a)):
        if a[i] < e:
            continue
        else:
            ind = i
            break
    if ind == -1:
        ind = len(a)
    return ind


def get_insert_index_binary(a, e):
    """
    To get the index using binary search
    :param a: sorted array
    :param e: element
    :return: index
    """

    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (high + low) // 2
        if a[mid] < e:
            low = mid + 1
        elif a[mid] > e:
            high = mid - 1
        else:
            return mid
    return len(a)


def solve():
    """
    The solution of the program
    :return: None
    """
    script_dir = os.path.dirname(__file__)
    rel_path = "res/running_median/input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        a_count = int(f.readline().strip())

        a = []

        for _ in range(a_count):
            a_item = int(f.readline().strip())
            a.append(a_item)

        result, result_1, result_2 = solution(a)
        print(result)
        # print(result_1)
        # print(result_2)

        print('Difference in output and result')

        for i in range(1000):
            if result[i] != op.o_p[i]:
                print(i, result[i], op.o_p[i])

        print('Difference in op and result 1')

        for i in range(1000):
            if result_1[i] != op.o_p[i]:
                print(i, result_1[i], op.o_p[i])

        print('Difference in op and result 2')

        for i in range(1000):
            if result_2[i] != op.o_p[i]:
                print(i, result_2[i], op.o_p[i])


