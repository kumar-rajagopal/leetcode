class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Binary:
	def __init__(self, val):
		self.root = Node(val)

	def print_traverse(self, type='in_order'):
		if type == 'in_order':
			return self.in_order_traverse(self.root)
		elif type == 'pre_order':
			return self.pre_order(self.root)
		elif type == 'post_order':
			return self.post_order(self.root)


	def in_order_traverse(self, root, traverse=''):
		#left->root->right
		if root:
			traverse = self.in_order_traverse(root.left, traverse)
			traverse += str(root.val) + ' '
			traverse = self.in_order_traverse(root.right, traverse)
		return traverse

	def pre_order(self, root, traverse=''):
		#root->left->right
		if root:
			traverse += str(root.val) + ' '
			traverse = self.pre_order(root.left, traverse)
			traverse = self.pre_order(root.right, traverse)
		return traverse

	def post_order(self, root, traverse=''):
		#left->right->root
		if root:
			traverse = self.post_order(root.left, traverse)
			traverse = self.post_order(root.right, traverse)
			traverse += str(root.val) + ' '
		return traverse 


tree = Binary(100)
tree.root.left = Node(70)
tree.root.right = Node(80)
tree.root.left.left = Node(50)
tree.root.left.right = Node(60)
tree.root.right.left = Node(75)

print(tree)
print(tree.print_traverse('in_order')) #50 70 60 100 75 80
print(tree.print_traverse('pre_order')) #100 70 50 60 80 75
print(tree.print_traverse('post_order')) # 50 60 70 75 80 100 