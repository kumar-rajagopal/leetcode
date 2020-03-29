"""
173. Binary Search Tree Iterator
Medium

1312

237

Favorite

Share
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    # return 3
iterator.next();    # return 7
iterator.hasNext(); # return true
iterator.next();    # return 9
iterator.hasNext(); # return true
iterator.next();    # return 15
iterator.hasNext(); # return true
iterator.next();    # return 20
iterator.hasNext(); # return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, data):
        self.root = Node(data)
        self.stack = []

    def in_order_traversal(self, start):
        if start:
            traversal = self.in_order_traversal(start.left)
            self.stack.append(start.val)
            traversal = self.in_order_traversal(start.right)
        return 1

    def print_tree(self):
        node = self.root
        self.in_order_traversal(node)
        return self

    def hasNext(self):
        #print(dir(stack))
        return len(self.stack) != 0

    def next(self):
        if self.hasNext():
            print('hn')
            next_item = self.stack.pop()
            return next_item
        return -1


tree = BSTIterator(7)
tree.root.left = Node(3)
tree.root.right = Node(15)
tree.root.right.left = Node(9)
tree.root.right.right = Node(20)

iterator = tree.print_tree()
print(iterator.next());    # return 3
print(iterator.next());    # return 7
print(iterator.hasNext()); # return true
print(iterator.next());    # return 9
print(iterator.hasNext()); # return true
print(iterator.next());    # return 15
print(iterator.hasNext()); # return true
print(iterator.next());    # return 20
print(iterator.hasNext()); # return false

"""
3
7
True
9
True
15
True
20
False
"""