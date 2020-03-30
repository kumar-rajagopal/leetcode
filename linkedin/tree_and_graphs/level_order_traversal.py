"""
Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]


"""
from collections import deque
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Binary:
    def __init__(self, data):
        self.root = Node(data)

    def print_val(self):
        root = self.root
        return self.level_order(root)
        #return self.levelOrder(root)

    def level_order(self, start):
        #level order - 
        level = 0
        result = []
        result.append((start.val, level))
        queue = deque([start])
        while(queue):
            data = []
            s = len(queue)
            for i in range(s):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                    data.append(node.left.val)
                if node.right != None:
                    queue.append(node.right)
                    data.append(node.right.val)
            if data:
                level += 1
                result.append((data,level))
        return result

    def levelOrder(self, start):
        res = []
        queue = deque([start])
        res.append((start.val, 0))
        level = 0
        while queue:
            size = len(queue)
            data = []
            for i in range(size):
                node = queue.popleft()
                if node.left != None:
                    queue.append(node.left)
                    data.append(node.left.val)
                if node.right != None:
                    queue.append(node.right)
                    data.append(node.right.val)
            if data:
                level +=1
                res.append((data, level))

        return res

tree = Binary(3)
tree.root.left = Node(9)
#tree.root.left.left = None
#tree.root.left.right = None
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)

"""
tree = Binary(3)
tree.root.left = TreeNode(9)
tree.root.right = TreeNode(20)
tree.root.right.left = TreeNode(15)
tree.root.right.right = TreeNode(7)
"""
print(tree.print_val())