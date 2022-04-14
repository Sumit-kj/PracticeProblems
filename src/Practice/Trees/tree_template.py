class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_children(self):
        return self.child

    def add_child(self, new_node):
        self.child.append(new_node)

    def set_children(self, node_list):
        self.child.extend(node_list)
