"""
Symmetric Tree
  Go to Discuss
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
time complexity of O(n) solution
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Symmetric:
	def __init__(self, node):
		self.root = TreeNode(node)

	def isSymmetric(self):
		start = self.root
		if start == None:
			return True
		return self.dfs(start.left, start.right)

	def dfs(self, l, r):
		if l and r:
			return l.val == r.val and self.dfs(l.left,r.right) and self.dfs(l.right,r.left)
		return l == r

	#Using stack - time complexity is also O(n)
	def isSymmetric1(self):
		start = self.root
		if start == None:
			return True
		stack = [(start.left,start.right)]
		while stack:
			l,r = stack.pop()
			if not l and not r:
				continue
			if not l or not r:
				return False
			stack.append([l.left,r.right])
			stack.append([l.right,r.left])
		return True

tree = Symmetric(1)
tree.root.left = TreeNode(2)
tree.root.left.left = TreeNode(3)
tree.root.left.right = TreeNode(4)

tree.root.right = TreeNode(2)
tree.root.right.left = TreeNode(4)
tree.root.right.right = TreeNode(3)

"""
#2nd sample
tree.root.left = TreeNode(2)
tree.root.left.right = TreeNode(3)
tree.root.right = TreeNode(2)
tree.root.right.right = TreeNode(3)
"""
print(tree.isSymmetric())

#ITERATIVE SOLUTION - using Stack
print(tree.isSymmetric1())