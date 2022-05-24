from src.Practice.Trees import binary_tree_creation


def binary_sum_trees():
    root_node = binary_tree_creation.create_tree()
    sum_of_binary_tree(root_node)
    return root_node


def sum_of_binary_tree(node):
    """
    This function gives the sum binary tree for a tree recursively
    :param node: The node to be considered
    :return: None
    """
    if node is None:
        return 0
    original_data = node.get_data()
    sum_data = sum_of_binary_tree(node.get_left()) + sum_of_binary_tree(node.get_right())
    new_data = original_data + sum_data if sum_data != 0 else 0
    node.set_data(new_data)
    return original_data + sum_data


