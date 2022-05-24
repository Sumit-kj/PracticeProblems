from src.Practice.Trees.binary_tree import BinaryTree as node


def create_tree():
    root_node = node(1)
    l_1 = node(2)
    r_1 = node(3)
    l_2 = node(4)
    r_2 = node(5)
    l_3 = node(6)
    r_3 = node(7)
    l_4 = node(8)
    r_4 = node(9)
    l_5 = node(10)
    r_5 = node(11)
    root_node.set_left(l_1)
    root_node.set_right(r_1)
    l_1.set_left(l_2)
    l_1.set_right(r_2)
    r_1.set_left(l_3)
    r_1.set_right(r_3)
    r_3.set_left(l_4)
    l_4.set_right(r_4)
    r_2.set_right(r_5)
    r_5.set_left(l_5)

    return root_node
