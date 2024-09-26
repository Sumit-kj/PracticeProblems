"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the
following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The
remaining elements of nums are not important as well as the size of nums. Return k."""
from src.res.Array.remove_element import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        nums, val = n[0], n[1]
        results.append(remove_element(nums, val))

    print(results)

    if op.o_p != results:
        print()
        print('Wrong answer')
        print('Expected output pattern:', op.o_p)
        print('Your output:', results)


def remove_element(nums, val):
    """
    This function remove all the occurrences of val
    :param nums: The list of elements
    :param val: The value to be removed
    :return: Count of elements that are not equal to val
    """
    i, j = 0, len(nums) - 1
    while i < j and i < len(nums):
        if nums[i] == val:
            while nums[j] == val and i < j:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        i += 1
    if i == len(nums):
        return -1
    i = 0
    while i < len(nums) and nums[i] != val:
        i += 1
    return i
