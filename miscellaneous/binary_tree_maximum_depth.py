"""
 Maximum Depth of Binary Tree
  Go to Discuss
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
maxDepth(root.left) and maxDepth(root.right) can be computed simultaneously only if you are running them in parallel, 
and if you are, you complexity depends on the number of available processors that can run in parallel. That said, 
your Java code is not running anything in parallel, since all of it runs on the same thread.

Assuming sequential execution, maxDepth has to traverse the entire tree, since it doesn't know if a certain path can 
lead to a max Depth until it reaches the leaf that ends that path. Therefore the time complexity is O(n).
"""

def maxDepth(self, root):
    if root == None:
      return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

