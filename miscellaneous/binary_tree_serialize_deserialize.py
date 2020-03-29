"""
Serialize and Deserialize Binary Tree
  Go to Discuss
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be 
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the 
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized 
to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches 
yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms 
should be stateless.
"""
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
        return "Root: {}".format(self.val)

class Codec:
    def __init__(self, data):
        self.root = TreeNode(data)

    def serialize(self):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node, res=[]):
            if node:
                res.append(str(node.val))
                helper(node.left, res)
                helper(node.right, res)
            else:
                res.append('#')
            return res
        res = helper(self.root)
        print(res)
        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(dataList):
            if dataList[0] == '#':
                dataList.popleft()
                return None
            root = TreeNode(dataList[0])
            dataList.popleft()
            root.left = helper(dataList)
            root.right = helper(dataList)
            return root
        deque_data = deque(data)
        root = helper(deque_data)
        return root

# Your Codec object will be instantiated and called as such:

tree = Codec(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.right.left = TreeNode(4)
tree.root.right.right = TreeNode(5)

print(tree.deserialize(tree.serialize()))