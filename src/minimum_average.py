"""
Tieu owns a pizza restaurant and he manages it in his own way. While in a normal restaurant, a customer is served by
following the first-come, first-served rule, Tieu simply minimizes the average waiting time of his customers. So he
gets to decide who is served first, regardless of how sooner or later a person comes.
Different kinds of pizzas take different amounts of time to cook. Also, once he starts cooking a pizza, he cannot cook
another pizza until the first pizza is completely cooked. Let's say we have three customers who come at time t=0, t=1,
& t=2 respectively, and the time needed to cook their pizzas is 3, 9, & 6 respectively. If Tieu applies first-come,
first-served rule, then the waiting time of three customers is 3, 11, & 16 respectively. The average waiting time in
this case is (3 + 11 + 16) / 3 = 10. This is not an optimized solution. After serving the first customer at time t=3,
Tieu can choose to serve the third customer. In that case, the waiting time will be 3, 7, & 17 respectively. Hence the
average waiting time is (3 + 7 + 17) / 3 = 9.
Help Tieu achieve the minimum average waiting time. For the sake of simplicity, just find the integer part of the
minimum average waiting time.
"""
import os
from src.res.minimum_average import output as op


def minimum_average(customers):
    """
    To give the minimum average waiting time for each customer
    :param customers: 2D array for customer arrival time, list of (time required to cook the pizza)
    :return: the minimum average waiting time
    """
    result = 0
    return result


def solve():
    """
    The solution of the program
    :return: None
    """
    script_dir = os.path.dirname(__file__)
    rel_path = "res/minimum_average/input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        n = int(f.readline().strip())

        customers = []

        for _ in range(n):
            customers.append(list(map(int, f.readline().rstrip().split())))

        result = minimum_average(customers)
        print(result)

        if result != op.o_p:
            print()
            print('Wrong answer')
            print('Expected output:', op.o_p)
            print('Your output:', result)
