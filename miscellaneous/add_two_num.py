class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        pass

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def add(self, first, second):
        
ll = LinkedList()
ll.insert(112)
ll.insert(7)
ll.insert(4)
nn = ll.printList()


def add_two_num(a, b):
    carry = 0
