# Python program to find sum of all left leaves
 
# A Binary tree node
class Node:
    # Constructor to create a new Node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to check if a given node is leaf or not
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 
# This function return sum of all left leaves in a
# given binary tree
def leftLeavesSum(root):
 
    # Initialize result
    res = 0
     
    # Update result if root is not None
    if root is not None:
 
        # If left of root is None, then add key of
        # left child
        
        if isLeaf(root.left): #This will be current root node without recur as we need to find the sum of all leaft leaves,
                              #identify the first left leaf and then the else condition will do the recursion
            res += root.left.key
        else:
            # Else recur for left child of root
            res += leftLeavesSum(root.left)
 
        # Recur for right child of root and update res. This will fetch all left leaves in root.right tree
        res += leftLeavesSum(root.right)
    return res
 
# Driver program to test above function 
 
# Let us constrcut the Binary Tree shown in the above function
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)        
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print ("Sum of left leaves is", leftLeavesSum(root))
