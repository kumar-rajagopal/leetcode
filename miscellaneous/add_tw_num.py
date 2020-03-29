class Node:
	def __init__(self, data):
		self.data = data
		self.root = None
		self.next = None
n = Node(3)
print(dir(n))
def add_two_num(a, b):
	carry = 0
