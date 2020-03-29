class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Binary:
    def __init__(self, val):
        self.root = Node(val)

    def print_tree(self):
        self.traverse_tree(self.root, '')

    def traverse_tree(self, start, traverse):
        #Left->root->right
        if start:
            #traverse = self.traverse_tree(start.left, traverse)
            traverse = self.traverse_tree(start.left, traverse)
            #traverse += str(start.val) + ' '
            traverse += str(start.val) + ' '
            #traverse = self.traverse_tree(start.right, traverse)
            traverse = self.traverse_tree(start.right, traverse)
        print(traverse)
        return traverse
    """
    def traverse_tree(self, start, traverse):
        print(start.val)
        if start:
            traverse = self.traverse_tree(start.left, traverse)

            traverse += str(start.val)
            traverse = self.traverse_tree(start.right, traverse)
        print(traverse)
        return traverse
    """

tree = Binary(3)
tree.root.left = Node(9)
tree.root.right = Node(8)

tree.root.left.left = Node(4)
tree.root.left.right = Node(1)

tree.root.right.left = Node(0)
tree.root.right.right = Node(7)

tree.root.right.left.left = Node(5)
tree.root.right.left.right = Node(2)
"""
tree = Binary(100)
tree.root.left = Node(80)
tree.root.right = Node(90)
"""
tree.print_tree()