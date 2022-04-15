from src.Practice.Trees import tree_creation


def breadth_first_search_traversal():
    root_node = tree_creation.create_tree()
    traverse = []
    traversal_algorithm(root_node, [root_node], traverse)
    print(traverse)


def traversal_algorithm(node, node_queue, traverse):
    """
    This function traverses recursively through the tree and stores traversal in an array
    :param node: The current node to be considered
    :param node_queue: The queue for consideration of nodes
    :param traverse: The traversal array
    :return: None
    """
    if len(node_queue) > 0:
        children_node_list = node.get_children()
        if children_node_list:
            node_queue.extend(children_node_list)
        traverse.append(node.get_data())
        node_queue = node_queue[1:]
        if len(node_queue) == 0:
            return
        traversal_algorithm(node_queue[0], node_queue, traverse)
