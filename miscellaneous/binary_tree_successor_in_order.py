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
			return (self.pre_order_traversal(self.root, ''))
		elif type == 'in_order':
			return (self.in_order_traversal(self.root, target))
		elif type == 'post_order':
			return (self.post_order_traversal(self.root, ''))
		else:
			return -1

	def in_order_traversal(self, start, target):
		"""Left->root->right. An inorder successor is the next node in the inorder traversal or In Binary Search 
		   Tree, Inorder Successor of an input node can also be defined as the node with the smallest key greater 
		   than the key of input node"""
		successor = None
		while start != None:
			if start.value < target:
				start = start.right
			elif start.value > target:
				successor = start #Succesor will be on the left sub tree for in order
				start = start.left
			else: #If target found, the successor element will be the last item in the left of the right side of the
				  # tree
				if start.right != None:
					while start.left != None:
						start = start.left
					successor = start
				break
		if successor is None:
			return None
		return successor.value


tree = BinaryTree(100)
tree.root.left = Node(50)
tree.root.left.left = Node(25)
tree.root.left.right = Node(75)
tree.root.right = Node(200)
tree.root.right.left = Node(125)
tree.root.right.right = Node(300)

#print(tree.print_tree('pre_order'))
print(tree.print_tree('in_order',125))
#print(tree.print_tree('post_order'))

 #pre-order - 100 50 25 75 200 125 300
 #in-order - 25 50 75 100 125 200 300
 #post-order - 25 75 50 125 300 200 100
