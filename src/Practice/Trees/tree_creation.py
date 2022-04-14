from src.Practice.Trees.tree_template import TreeNode as node


def create_tree():
    root_node = node(10)
    node_1 = node(20)
    node_2 = node(30)
    node_3 = node(40)

    root_node.set_children([node_1, node_2, node_3])

    print(root_node)
