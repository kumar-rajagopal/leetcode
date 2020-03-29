"""
Construct Binary Tree from Inorder and Postorder Traversal
  Go to Discuss
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7] -> 
postorder = [9,15,7,20,3] -> root->left->right from the rear or stack
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

Time Complexity: O(n^2). Worst case occurs when tree is left skewed. 
Example Preorder and Inorder traversals for worst case are {A, B, C, D} and {D, C, B, A}.

Time Complexity : O(n2)

Optimized approach: We can optimize the above solution using hashing (unordered_map in C++ or HashMap in Java).
We store indexes of inorder traversal in a hash table. So that search can be done O(1) time.
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    def __repr__(self):
        return "Root {}, Left {}, Right {}".format(self.val,self.left.val,self.right.val)

def buildTree(postOrder, inOrder):
    if not postOrder or not inOrder:
        return None 
    root = Node(postOrder.pop()) #pop is O(1) but pop(0) is O(n)
    inOrderIndex = inOrder.index(root.val)

    root.right = buildTree(postOrder, inOrder[inOrderIndex+1:]) #Using : does not create a new list
    root.left = buildTree(postOrder, inOrder[:inOrderIndex])

    return root

from collections import deque
def buildTree1(preorder, inorder):
    #preorder - root->left->right; inorder - left->root->right
    if not preorder or not inorder:
            return None
    
    preorder_root = preorder.pop(0)
    root = Node(preorder_root)

    inorder_index = inorder.index(root.val)
    root.left = buildTree1(preorder, inorder[:inorder_index])
    root.right = buildTree1(preorder, inorder[inorder_index+1:])

    
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(buildTree(postorder, inorder))

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(buildTree1(preorder, inorder))

