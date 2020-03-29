#Print sum of all left leaf
from collections import deque
class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)

    def print_left_sum(self):
        result = None
        r = self.bt_sum(self.root)
        #print(r)
        return r

    def check_leaf(self, tree_node):
        if tree_node is None:
           return False
        if tree_node.left is None:
            return True
        if tree_node.right is None:
            return True
        if tree_node.left is None and tree_node.right is None:
            return True

    def bt_sum(self, tree_node):
        res = 0
        if tree_node is not None:
            if self.check_leaf(tree_node.left):
                print(tree_node.left.value)
                res += tree_node.left.value
            else: #Recur all left nodes of the root
                res += self.bt_sum(tree_node.left)
            res += self.bt_sum(tree_node.right)

        return res

    """
    def bt_sum(self, tree_node):
        if tree_node is None:
           return False
        if tree_node.left is None:
            return True
        if tree_node.right is None:
            return True
        if tree_node.left is None and tree_node.right is None:
            return True
        res = 0
        if tree_node is not None:
            res += self.bt_sum(tree_node.left)
            print(res)
        return res
    """
tree = BinaryTree(20)
tree.root.left = Node(9)
tree.root.right = Node(49)
tree.root.right.left = Node(23)        
tree.root.right.right = Node(52)
tree.root.right.right.left = Node(50)
tree.root.left.left = Node(5)
tree.root.left.right = Node(12)
tree.root.left.right.right = Node(12)

print(tree.print_left_sum())
