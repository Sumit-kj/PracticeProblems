from src.Practice.Trees.binary_tree import BinaryTree as node


def create_tree():
    root_node = node(1)
    l_1 = node(2)
    r_1 = node(3)
    l_2 = node(4)
    r_2 = node(5)
    l_3 = node(6)
    r_3 = node(7)
    root_node.set_left(l_1)
    root_node.set_right(r_1)
    l_1.set_left(l_2)
    l_1.set_right(r_2)
    r_1.set_left(l_3)
    r_1.set_right(r_3)

    return root_node
