"""
Binary Tree Level Order Traversal
  Go to Discuss
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

Time Complexity: If queue is used, then O(n) where n is number of nodes in the binary tree and O(n^2) if 
recursion is used

"""
from collections import deque
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Binary:
    def __init__(self, data):
        self.root = TreeNode(data)

    def print_tree(self):
        start = self.root
        return self.levelOrder(start)

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
tree.root.left = TreeNode(9)
tree.root.right = TreeNode(20)
tree.root.right.left = TreeNode(15)
tree.root.right.right = TreeNode(7)

print(tree.print_tree())

