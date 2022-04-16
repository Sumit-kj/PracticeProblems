from src.Practice.Trees import binary_tree_creation


def inorder_traversal():
    root_node = binary_tree_creation.create_tree()
    traverse = []
    traversal_algorithm(root_node, traverse)
    print(traverse)


def traversal_algorithm(node, traverse):
    """
    This is the implementation of inorder traversal for a binary tree
    :param node: The node to be considered
    :param traverse: The traversal array for storing nodes travelled
    :return:
    """
    if node:
        traversal_algorithm(node.get_left(), traverse)
        traverse.append(node.get_data())
        traversal_algorithm(node.get_right(), traverse)
