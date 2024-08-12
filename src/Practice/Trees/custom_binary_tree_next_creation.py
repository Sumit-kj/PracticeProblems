from src.Practice.Trees.binary_tree import BinaryTreeNext as node


def create_tree(node_list):
    root_node = None
    if len(node_list) == 0:
        return root_node
    for index, val in enumerate(node_list):
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        if left_index >= len(node_list):
            return node(val)
        
    return root_node
