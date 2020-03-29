class Node(object):
	def __init__(self, data):
		self.value = data
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, type, target):
		if type == 'pre_order':
			return (self.pre_order_traversal(self.root, target))

		else:
			return -1

	def pre_order_traversal(self, start, target):
		"""root->left->right"""
		successor = None
		if target < start.value:
			start = start.left
		elif target > start.value:
			start = start.right
		while start != None:
			print(start.value)
			successor = start.value
			if start.value == target:
				
				if start.right != None:
					successor = start.right.value

				elif start.left != None:
					if start.left.right != None:
						successor = start.left.right.value
					elif start.left.left != None:
						successor = start.left.left
				return successor
			start = start.left
			#self.pre_order_traversal(start, target)

		return successor

"""
	def pre_order_traversal(self, start, traversal):
		""root->Left->right"
		if start:
			traversal += ' ' + str(start.value)
			traversal = self.pre_order_traversal(start.left, traversal)
			traversal = self.pre_order_traversal(start.right, traversal)
		return traversal
"""
tree = BinaryTree(100)
tree.root.left = Node(50)
tree.root.left.left = Node(25)
tree.root.left.right = Node(75)
tree.root.right = Node(200)
tree.root.right.left = Node(125)
tree.root.right.right = Node(350)

print(tree.print_tree('pre_order', 100)) # max value in right sub tree
#print(tree.print_tree('in_order',125))
#print(tree.print_tree('post_order'))

 #pre-order - 100 50 25 75 200 125 300
 #in-order - 25 50 75 100 125 200 300
 #post-order - 25 75 50 125 300 200 100
