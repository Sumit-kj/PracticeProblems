"""
The factorial problem asks you to find the product of all positive integers from 1 up to a given non-negative integer
$$ n $$. This means you want to determine how many ways things can be arranged or multiplied in a sequence running from
1 all the way to $$ n $$.

For example, if you pick $$ n = 5 $$, the factorial of 5 (written as 5!) is the multiplication of 1 × 2 × 3 × 4 × 5.
This kind of operation is common in counting problems—like how many ways you can arrange a set of items or calculate
permutations.

The problem also involves recognizing a pattern: the factorial of a number relates to the factorial of the previous
number multiplied by the current number, which naturally breaks down into smaller subproblems. This is foundational for
recursive problem solving and eventually dynamic programming.

Understanding factorials is key for grasping many concepts in mathematics, combinatorics, probability, and algorithms.

That’s the essence of the factorial problem—finding the total product of all integers up to a given number and
appreciating the recursive pattern within it.[2][6][7]
"""
from src.res.Practice.Recursion.factorial import input as ip, output as op


def solve():
    """
    The solution of the program
    :return: None
    """
    result = list()
    for n in ip.i_p:
        result.append(factorial(n))
    print(result)

    if result != op.o_p:
        print()
        print('Wrong answer')
        print('Expected output:', op.o_p)
        print('Your output:', result)


def factorial(num):
    """
    This function recursively calculates the factorial of a given number
    :param num: The number for which factorial is to be calculated
    "return: The factyorial of the number
    """
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)