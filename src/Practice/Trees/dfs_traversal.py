from src.Practice.Trees import tree_creation


def depth_first_search_traversal():
    root_node = tree_creation.create_tree()
    traverse = []
    traversal_algorithm(root_node, [root_node], traverse)
    print(traverse)


def traversal_algorithm(node, node_stack, traverse):
    """
    This function traverses recursively through the tree and stores traversal in an array
    :param node: The current node to be considered
    :param node_stack: The stack for consideration of nodes
    :param traverse: The traversal array
    :return: None
    """
    if len(node_stack) > 0:
        traverse.append(node.get_data())
        node_stack.pop()
        children_node_list = node.get_children()
        if children_node_list:
            node_stack.extend(children_node_list)
        if len(node_stack) == 0:
            return
        traversal_algorithm(node_stack[-1], node_stack, traverse)
