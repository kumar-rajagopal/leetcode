"""
Min Stack
  Go to Discuss
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = [(None,float('inf'))]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.minStack.append((x, min(x, self.minStack[-1][1]))) #Store actual value and the minimum as tuple
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.minStack) > 0:
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.minStack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()