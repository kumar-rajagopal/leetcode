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
class TreeNode:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

class BSTIterator:
	"""docstring for BSTIterator __init__(self, arg):"""
	def __init__(self, root):
		self.root = TreeNode(root)
		self.stack = []

		current = self.root
		while current != None:
			self.stack.append(current)
			current = current.left
		print("SLEN ",len(self.stack))
		return

	def hasNext(self):
		return len(self.stack) != 0 #Return true if stack is not empty

	def next(self):
		if self.hasNext():
			next_node = self.stack.pop()
			current = next_node.right
			while current != None:
				self.stack.append(current)
				current = current.left
			return next_node.val
		return -1

tree = BSTIterator(7)
tree.root.left = TreeNode(3)
tree.root.right = TreeNode(15)
tree.root.right.left = TreeNode(9)
tree.root.right.right = TreeNode(20)

#iterator = BSTIterator(tree);
"""
while iterator.hasNext():
	print(iterator.next())
	iterator = iterator.next()

iterator.next();    # return 3
iterator.next();    # return 7
iterator.hasNext(); # return true
iterator.next();    # return 9
iterator.hasNext(); # return true
iterator.next();    # return 15
iterator.hasNext(); # return true
iterator.next();    # return 20
iterator.hasNext(); # return false


3 7 9 15 20
"""
#print(tree.right.left.val)

"""
i, v = BSTIterator(tree), []
while i.hasNext():
	#print("NE ",i.hasNext())
	i = i.next()
	v.append(i.next())
print(v)

"""

print(tree)
print(tree.hasNext())
print(tree.next())
print(tree.next())
print(tree.hasNext())
print(tree.next())
print(tree.hasNext())
print(tree.next())
print(tree.hasNext())
print(tree.next())
print(tree.hasNext())

