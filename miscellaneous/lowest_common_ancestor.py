"""
Lowest Common Ancestor of a Binary Tree
  Go to Discuss
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA 
definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Ancestor:
    def __init__(self, data):
        self.root = Node(data)

    def postOrder(self, p, q):
        start = self.root
        if start == None:
            return

        stack = [(start)]
        while (stack):
            node = stack.pop()
            res = node.val
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
            if node.left and node.right:
                if node.left.val == p and node.right.val == q:
                #print(node.val, node.left.val, node.right.val)
                #print(stack.pop().val)
                    return node.val
        return False

    #def inorder(self, p, q):

    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        #print(root.val)
        left, right = (self.lowestCommonAncestor(kid, p, q)
                        for kid in (root.left, root.right))
        return root if left and right else left or right


tree = Ancestor(3)
tree.root.left = Node(5)
tree.root.left.left = Node(6)
tree.root.left.right = Node(2)
tree.root.left.right.left = Node(7)
tree.root.left.right.right = Node(4)

tree.root.right = Node(1)
tree.root.right.left = Node(0)
tree.root.right.right = Node(8)

#tree.print_tree()
print(tree.postOrder(5, 4))
print(tree.lowestCommonAncestor(tree,5,4))


