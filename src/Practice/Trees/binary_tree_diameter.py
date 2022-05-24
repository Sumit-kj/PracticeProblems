from src.Practice.Trees import binary_tree_creation


def binary_tree_ancestors(node, key, traverse, found):
    """
    This function gives the ancestors of a node in a binary tree
    :param node: The root node
    :param key: The node for which the depth is to be calculated
    :param traverse: The node for which the depth is to be calculated
    :param found: The flag
    :return: The list of ancestors to the node
    """
    if node:
        if node.get_data() == key:
            return True, traverse
        traverse.append(node.get_data())
        found, traverse = binary_tree_ancestors(node.get_left(), key, traverse, found)
        if found:
            return found, traverse
        found, traverse = binary_tree_ancestors(node.get_right(), key, traverse, found)
        if found:
            return found, traverse
        traverse.pop()
    return found, traverse


def binary_tree_diameter():
    root_node = binary_tree_creation.create_tree()
    key = 11
    traverse = []
    found, traverse = binary_tree_ancestors(root_node, key, traverse, False)
    print(traverse)
