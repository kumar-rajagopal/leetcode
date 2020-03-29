"""
Path Sum
  Go to Discuss
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along 
the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Non-recursive solution. DFS. O(n) time, O(log(n)) average space, O(n) worst case space

"""
from collections import deque
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self, data):
        self.root = TreeNode(data)

    #DFS Uses stack as queue
    def pathSum(self, target):
        start = self.root
        if start:
            stack = [(start, [start.val])]
        res = []
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right and sum(ls) == target:        
                res.append(ls)
            if node.left:
                stack.append([node.left, ls+[node.left.val]])
            if node.right:
                stack.append([node.right, ls+[node.right.val]])
        return res

    #BFS with queue better time complexity
    def pathSumQ(self, sum):
        root = self.root
        res, queue = [], deque([(root, sum, [])])
        while queue:
            node, sum, path = queue.popleft()
            if node:
                if node.val == sum and not node.left and not node.right:
                    res.append(path+[node.val])
                    continue
                print(node.left.val, node.val)
                queue.append((node.left, sum-node.val, path+[node.val]))
                queue.append((node.right, sum-node.val, path+[node.val]))
        return res

tree = Solution(5)
tree.root.left = TreeNode(4)
tree.root.left.left = TreeNode(11)
tree.root.left.left.left = TreeNode(7)
tree.root.left.left.right = TreeNode(2)

tree.root.right = TreeNode(8)
tree.root.right.left = TreeNode(13)
tree.root.right.right = TreeNode(4)
tree.root.right.right.right = TreeNode(1)

print(tree.pathSum(22))
print(tree.pathSumQ(22))

