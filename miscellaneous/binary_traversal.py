from pprint import pprint
class Node:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

class binaryTree:
	def __init__(self, val):
		self.root = Node(val)

	def __repr__(self):
		print('<a:%s, b:%s>' %(self.root, self.root.value))

	def print_tree(self):
		res = ''
		print(self.traverse(self.root, res))

	def traverse(self, root, res):
		if root:
			res += ' ' + str(root.value)
			res = self.traverse(root.left, res)
			
			res = self.traverse(root.right, res)
		return res


tree = binaryTree(30)
tree.root.left = Node(25)
tree.root.right= Node(40)
tree.root.left.left = Node(20)
tree.root.right.left = Node(18)
#r = tree.__repr__()
pprint(tree.root.left)
tree.print_tree()

"""
    def print_tree(self, type='pre_order'):
        if type == 'pre_order':
            return (self.pre_order_traversal(self.root, ''))
        elif type == 'in_order':
            return (self.in_order_traversal(self.root, ''))
        elif type == 'post_order':
            return (self.post_order_traversal(self.root, ''))
        elif type == 'level_order':
            return (self.level_order_traversal(self.root, ''))
        else:
            return -1

    def pre_order_traversal(self, start, traversal):
        ""root->Left->right"
        if start:
            traversal += ' ' + str(start.value)
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal
"""