class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next = next_node

	def get_data(self):
		return (self.data)

	def get_node(self):
		return (self.next)

	def set_data(self, datum):
		self.data = datum
		return(self.data)

	def set_node(self, new_node):
		self.node = new_node
