class MyCircularQueue:
    """
    References: https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1396/
    """
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.data = [None]*k
        self.head = -1 
        self.tail = -1
        
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        Queue could be in three state:
            Empty => move head and tail
            Full => return False
            Normal => move tail 
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():  
            self.data[0] = value
            self.head = 0
            self.tail = 0
            return True
        elif self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.size
            self.data[self.tail] = value
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        Queue could be in three states:
            Empty => return False
            only 1 element => remove value and reset head/tail
            more than 1 element => move head
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.data[self.head] = None
            
            if self.head == self.tail:  # queue is Empty, reset head and tail
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.size
            return True
            
    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.isEmpty() else self.data[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        head and tail will always reset to -1 if queue is empty.
        :rtype: bool
        """
        return self.head == -1 and self.tail == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        # %size is common in circular design
        return self.head == (self.tail + 1) % self.size