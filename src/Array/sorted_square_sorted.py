"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
from src.res.Array.sorted_square_sorted import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(sorted_square_sorted(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output pattern:', op.o_p)
        print('Your output:', results)


def sorted_square_sorted(nums):
    """
    This function squares a list and arranges it in increasing order
    Args:
        nums: The list of elements
    Returns:
        Sorted squared array as input
    """
    res = []
    for i in nums:
        l, h = 0, len(res)
        mid = (l + h) // 2
        val = i * i
        if len(res) == 0:
            res.append(val)
        else:
            while l < h:
                mid = (l + h) // 2
                if (mid > -1 and res[mid] > val > res[mid - 1]) or res[mid] == val:
                    break
                elif res[mid] > val:
                    h = mid - 1
                elif res[mid] < val:
                    l = mid + 1
                if l == h:
                    mid = (l + h) // 2
                    l += 1
            res.insert(mid, val)
    return res
