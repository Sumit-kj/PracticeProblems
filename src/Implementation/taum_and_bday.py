"""
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from
Taum: one is black and the other is white. To make her happy, Taum has to buy b black gifts and w white gifts.

The cost of each black gift is bc units.
The cost of every white gift is wc units.
The cost to convert a black gift into white gift or vice versa is z units.
Determine the minimum cost of Diksha's gifts.

Example
b = 3
w = 5
bc = 3
wc = 4
z = 1

He can buy a black gift for 3 and convert it to a white gift for 1, making the total cost of each white gift 4. That
matches the cost of a white gift, so he can do that or just buy black gifts and white gifts. Either way, the overall
cost is 3*3 + 5*4 = 29.
"""
import os
from ..res.Implementation.taum_and_bday import output as op


def taum_bday(b, w, bc, wc, z):
    """
    This function calculates the total cost of gifts
    :param b: The number of black gifts
    :param w: The number of white gifts
    :param bc: The cost of black gift
    :param wc: The cost of white gifts
    :param z: The cost of converting one gift to another
    :return: The total cost for the gifts
    """
    cost_b = bc if bc <= wc + z else wc + z
    cost_w = wc if wc <= bc + z else bc + z
    return b*cost_b + w*cost_w


def solve():
    """
    The solution of the program
    :return: None
    """
    script_dir = os.path.dirname(__file__)
    rel_path = "../res/Implementation/taum_and_bday/input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        t = int(f.readline().strip())

        for i in range(t):
            b, w = list(map(int, f.readline().strip().split()))
            bc, wc, z = list(map(int, f.readline().strip().split()))

            result = taum_bday(b, w, bc, wc, z)
            print(result)

            if result != op.o_p[i]:
                print()
                print('Wrong answer')
                print('Expected output:', op.o_p)
                print('Your output:', result)
