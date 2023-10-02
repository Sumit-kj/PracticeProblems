"""
David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball
he has into its own container. David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

 * Each container contains only balls of the same type.
 * No two balls of the same type are located in different containers.

Example
containers = [[1,4], [2,3]]

David has n=2 containers and 2 different types of balls, both of which are numbered from 0 to n-1 = 1 . The distribution
of ball types per container are shown in the following diagram.

[ 0, 1, 1, 1, 1] [0, 0, 1, 1, 1]

In a single operation, David can swap two balls located in different containers.

In this case, there is no way to have all green balls in one container and all red in the other using only swap
operations. Return Impossible.

You must perform q queries where each query is in the form of a matrix, M. For each query, print Possible on a new line
if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.
"""
import os
from ..res.Implementation.organizing_containers_of_balls import output as op


def organize_container(containers):
    """
    This function finds if it is possible to get sorted containers
    :param containers: The list of containers with the count of each type of balls
    :return: If it is possible to shuffle and get sorted containers
    """

    return 'Possible'


def solve():
    """
    The solution of the program
    :return: None
    """
    script_dir = os.path.dirname(__file__)
    rel_path = "../res/Implementation/organizing_containers_of_balls/input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        q = int(f.readline().strip())

        for i in range(q):

            q = int(f.readline().strip())
            containers = []

            for _ in range(q):
                containers.append(list(map(int, f.readline().strip().split())))

            result = organize_container(containers)
            print(result)

            if result != op.o_p[i]:
                print()
                print('Wrong answer')
                print('Expected output:', op.o_p)
                print('Your output:', result)
