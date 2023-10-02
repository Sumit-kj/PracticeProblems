"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, ..., Sm}
valued coins, how many ways can we make the change? The order of coins doesn't matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.
"""

from src.res.DynamicProgramming.rod_cutting import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    price = arr[0]
    length = arr[1]
    result = rod_cutting(price, length)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def rod_cutting(price, length):
    """
    This function returns the maximum value of rod cutting
    :param price: The price for corresponding length
    :param length: The length of the rod
    :return: The maximum value
    """
    price_density = [x/(index + 1) for index, x in enumerate(price)]
    max_value = 0
    while length > 0:
        max_price_density_index = price_density.index(max(price_density[0:length]))
        max_price_length = max_price_density_index + 1
        max_value += price[max_price_density_index]
        length -= max_price_length
    return max_value
