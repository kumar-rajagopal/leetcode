class Node:
	def __init__(self, item):
		self.data = item
		self.next = None

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.head = data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next


class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None
	
	def add(self, item):
		current = self.head
		prev = None
		stop = False

		while current != None and not stop:
			if current.get_data() > item:
				stop = True
			else:
				prev = current
				current = current.get_next()

		temp = Node(item)
		if prev == None:
			temp.set_next(self.head)
			self.head = temp
		else:
			temp.set_next(current) #create a link to the current node from the new node
			prev.set_next(temp) #create a link to point the prev point to the new node

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.get_data() == item:
				found = True
			else:
				if current.get_data() > item:
					stop = True
				else:
					current = current.get_next()
		return found

	def remove(self, item):
		prev = None
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				prev = current
				found = True
			else:
				current = current.get_next()
		if found:
			if prev is None:
				self.head = current.get_next()
			else:
				prev.set_next(current.get_next)

	def is_empty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.get_next()
		return count


myList = LinkedList()
myList.add(24)
myList.add(30)
myList.add(60)
myList.add(100)
print(myList.size())
print(myList.search(100))
print(myList.remove(60))
print(myList.size())

"""
3.23.1. Analysis of Linked Lists
To analyze the complexity of the linked list operations, we need to consider whether they require traversal. 
Consider a linked list that has n nodes. The isEmpty method is 𝑂(1) since it requires one step to check the 
head reference for None. size, on the other hand, will always require n steps since there is no way to know
how many nodes are in the linked list without traversing from head to end. Therefore, length is 𝑂(𝑛). 
Adding an item to an unordered list will always be O(1) since we simply place the new node at the head of 
the linked list. However, search and remove, as well as add for an ordered list, all require the traversal
process. Although on average they may need to traverse only half of the nodes, these methods are all 𝑂(𝑛)
since in the worst case each will process every node in the list.
"""



