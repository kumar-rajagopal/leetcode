"""
Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  

Clarification:

Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5

The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

Graph Explanation with 3 Python Solutions
41
VIEWS
2

Last Edit: February 7, 2020 6:25 PM
lun_jiang
lun_jiang
 11

The toughest part of this question is to understand the definition of upside down. So I made a graph to explain my thoughts.

To my understanding, the binary tree is to turned "upside down" level by level, where in each level:

    The original left child to be the new root;
    The original root to be the new right child;
    The original right child to be the new left child;

as shown below:

image

Now that the idea of upside down is clear, ths question appears to be a tree traversal problem. We can perform the traversal recursively or iteratively.
Another point is that since a tree is a DAG(direct acyclic graph), we won't be able to retrieve info from upper level. This is not a problem in a botton-up approach, but if we use a top-down approach, it's necessary to store the information of the parent node and right sibling node to enable us to build reversed links from a lower level to upper level.

Here are 3 solutions in Python3, recursive bottom-up, recursive top-down, and Iterative top-down:
"""
"""
Recursive Bottom-up
"""

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        if not root.left: return root
        
        old_left_leaf = self.upsideDownBinaryTree(root.left)
                
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        
        return old_left_leaf

"""
Recursive Top-down
"""

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        
        self.old_left_leaf = None  # the new root
        
        def helper(root, old_parent, old_right_sibling):
            if not root: return            
            
            _left_child = root.left
            _right_child = root.right
            root.left = old_right_sibling
            root.right = old_parent

            if _left_child: 
                helper(_left_child, root, _right_child)
            else:
                self.old_left_leaf = root                

        helper(root, None, None)
        
        return self.old_left_leaf

"""
Iterative Top-down
"""

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        
        old_left_leaf = None  # the new root
        old_parent = None
        old_right_sibling = None 
        
        while root:
            # change the current level
            _left_child = root.left
            _right_child = root.right
            root.left = old_right_sibling
            root.right = old_parent
            
            # check if reach the left leaf
            if not _left_child:
                old_left_leaf = root
                break
            
            # move down to the next level
            old_parent = root
            root = _left_child
            old_right_sibling = _right_child                        
        
        return old_left_leaf

#For the below solution: Complexity: O(N) time and O(1) space, where N is the number of nodes in the input tree.
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
		# start from root
        cur, pre, preRight = root, None, None
        while cur:
			# temporarily store 'cur.left' and 'cur.right' ('cur.left' will be next 'cur')
            temp1, temp2 = cur.left, cur.right
			# modify parent-child links
            cur.left, cur.right = preRight, pre
			# go to next iteration
            cur, pre, preRight = temp1, cur, temp2
        return pre
