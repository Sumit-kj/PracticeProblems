from src.Practice.Trees.tree_template import TreeNode as node


def create_tree():
    root_node = node(1)
    node_1 = node(2)
    node_2 = node(3)
    node_3 = node(4)
    node_4 = node(5)
    node_5 = node(6)
    node_6 = node(7)
    node_7 = node(8)
    node_8 = node(9)
    node_9 = node(10)
    node_10 = node(11)

    root_node.set_children([node_1, node_2, node_3])
    node_1.set_children([node_4, node_5])
    node_2.set_children([node_9, node_10])
    node_3.set_children([node_8])
    node_4.set_children([node_6, node_7])

    return root_node
