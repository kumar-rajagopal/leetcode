"""
Path Sum
  Go to Discuss
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Non-recursive solution. DFS. O(n) time, O(log(n)) average space, O(n) worst case space

"""
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self, data):
        self.root = TreeNode(data)

    def pathSum(self, sum):
        start = self.root
        if start:
            stack = [(start,0)]
        res = []
        res1 = []
        while stack:
            node = stack.pop()
            print("n: ",node[0].val)
            path,sum_val = node[0],node[1]
            curr_node_val = path.val + sum_val
            if path.left == None and path.right == None: #Hitting the leaf node
                if curr_node_val == sum:
                    print(res, res1)
                    return True
            if path.left:
                res.append(path.left.val)
                stack.append([path.left, curr_node_val])
            if path.right:
                res1.append(path.right.val)
                stack.append([path.right, curr_node_val])
        return res

tree = Solution(5)
tree.root.left = TreeNode(4)
tree.root.left.left = TreeNode(11)
tree.root.left.left.left = TreeNode(7)
tree.root.left.left.right = TreeNode(2)

tree.root.right = TreeNode(8)
tree.root.right.left = TreeNode(13)
tree.root.right.right = TreeNode(4)
tree.root.right.right.right = TreeNode(1)

print(tree.pathSum(22))

