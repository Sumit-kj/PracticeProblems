"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, ..., Sm}
valued coins, how many ways can we make the change? The order of coins doesn't matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.
"""

from src.res.DynamicProgramming.coin_change import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    arr = ip.i_p
    amount = arr[0]
    coins = arr[1]
    # result = coin_change(amount, coins, len(coins) - 1)
    result = coin_change_dp(amount, coins)
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def coin_change(amount, coins, index):
    """
    This function gives the number of possible counts of combinations of change sums to amount recursively
    :param amount: The amount
    :param coins: The change list
    :param index: current coin to be considered or not
    :return: The count of combinations to provide exact change to amount
    """
    if amount == 0:
        return 1
    if len(coins) == 0 or index < 0 or amount < 0:
        return 0
    return coin_change(amount - coins[index], coins, index) + coin_change(amount, coins, index - 1)


def coin_change_dp(amount, coins):
    """
    This function gives the number of possible counts of combinations of change sums to amount using dp
    :param amount: The amount
    :param coins: The change list
    :return: The count of combinations to provide exact change to amount
    """
    coin_amount = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

    for i in range(len(coins)):
        coin_amount[0][i] = 1

    for i in range(len(coins)):
        for j in range(1, amount + 1):
            if i == 0 and j % coins[i] == 0:
                coin_amount[i][j] = 1
            elif i == 0:
                coin_amount[i][j] = 0
            else:
                excluding_count = coin_amount[i-1][j]
                if j < coins[i]:
                    including_count = 0
                else:
                    including_count = coin_amount[i][j-coins[i]]
                coin_amount[i][j] = excluding_count + including_count

    return coin_amount[len(coins) - 1][amount]
