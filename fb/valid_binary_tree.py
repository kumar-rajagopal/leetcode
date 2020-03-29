"""
98. Validate Binary Search Tree
Medium

1949

295

Favorite

Share
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Big(O) - O(n) time complexity

"""

class TreeNode:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class ValidBinary:
	def __init__(self, data):
		self.root = TreeNode(data)

	def print_valid(self):
		root = self.root
		return self.isValidTree(root, float("-inf"), float("inf"))

	def isValidTree(self, start, low, high):
		"""in order traversal -> left -> root -> right"""
		if start is None:
			return True
		if not start.left and not start.right:
			return low < start.val < high

		return (low < start.val < high and self.isValidTree(start.left, low, start.val) and 
										  self.isValidTree(start.right, start.val, high))

tree = ValidBinary(2)
tree.root.left = TreeNode(1)
tree.root.right = TreeNode(3)

"""
tree = ValidBinary(5)
tree.root.left = TreeNode(1)

tree.root.right = TreeNode(4)
tree.root.right.left = TreeNode(3)
tree.root.right.right = TreeNode(6)
"""

print(tree.print_valid())

"""

# iteratively, in-order traversal
# O(n) time and O(n)+O(lgn) space
def isValidBST(self, root):
    stack, res = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        # if root is None or all the nodes have 
        # been traversed and have no confliction 
        if not stack:
            return True
        node = stack.pop()
        # res stores the current values in in-order 
        # traversal order, node.val should larger than
        # the last element in res
        if res and node.val <= res[-1]:
            return False
        res.append(node.val)
        root = node.right

"""