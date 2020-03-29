"""
236. Lowest Common Ancestor of a Binary Tree
Medium

1870

133

Favorite

Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "val {} ".format(self.val)

class BinaryTree:
    def __init__(self, node):
        self.root = TreeNode(node)

    def processTree(self,p,q):
        result = self.lowestAncestor(self.root, p, q)
        return result

    def lowestAncestor(self, root, p, q):
        """Post order traversal - left->right->root"""
        if root is None:
            return
        if root.val == p or root.val == q:
            return root.val
        left = self.lowestAncestor(root.left, p, q)
        right = self.lowestAncestor(root.right, p, q)
        
        if left != None and right != None:
            return root
        if left == None and right != None:
            print("RI ",right)
            return right
        elif right == None and left != None:
            print("L ",left)
            return left
        return None

tree = BinaryTree(3)
tree.root.left = TreeNode(5)
tree.root.right = TreeNode(1)
tree.root.left.left = TreeNode(6)
tree.root.left.right = TreeNode(2)
tree.root.right.left = TreeNode(0)
tree.root.right.right = TreeNode(8)

print(tree.processTree(5,1))

"""
6 2 5 0 8 1 3
"""





