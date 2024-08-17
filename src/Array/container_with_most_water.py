"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
from src.res.Array.container_with_most_water import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    results = []

    for n in arr:
        results.append(container_with_most_water(n))
    print(results)

    if results != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', results)


def container_with_most_water(height):
    """
    This function returns the maximum area of water that can be blocked in this structure
    Args:
        height: A list that represents the height of each consecutive poles
    Returns:
        The maximum area of water that can be stored in this structure
    """
    l, h = 0, len(height) - 1
    max_area = 0
    while l < h:
        lower_height = height[l] if height[l] <= height[h] else height[h]
        area_calculated = lower_height * (h - l)
        if area_calculated > max_area:
            max_area = area_calculated
        if height[l] < height[h]:
            l += 1
        else:
            h -= 1
    return max_area
        
