"""
341. Flatten Nested List Iterator
Medium

922

382

Favorite

Share
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        #Need to reverse the input order of elements because stack uses LIFO and 
        #output needs to be in the same order as input
        self.stack = [ni for ni in reversed(nestedList)] 

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            for ni in reversed(top.getList()):
                self.stack.append(ni)

        return False

class NestList:
    def __init__(self):
        self.result_list = []

    def nested_list(self, start, n=0):
        print("ST: ",start)
        for i in range(n,len(start)):
            if type(start[i]) is list:
                self.nested_list(start[i], 0)
            else:
                n += 1
                self.result_list.append(start[i])
        return True


nl = NestList()
nl.nested_list([1,[4,[6]]])
print(nl.result_list)