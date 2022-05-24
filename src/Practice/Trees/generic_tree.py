class NAryTree:
    def __init__(self, data):
        self.data = data
        self.first_child = None
        self.next_sibling = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_first_child(self, node):
        self.first_child = node

    def get_first_child(self):
        return self.first_child

    def set_next_sibling(self, node):
        self.next_sibling = node

    def get_next_sibling(self):
        return self.next_sibling
