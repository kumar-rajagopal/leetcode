from itertools import permutations
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Binary:
    def generateTrees(self, n):
        l = []
        i = 1
        while i <= n:
            l.append(i)
            i+=1
        p = list(permutations(l,n))
        for item in p:
            data = item[0]
            root = Node(data)
            val = root.data
            k = 1
            for k in range(1,len(item)):
                print("ik: ",item[k])
                if item[k] <= val:
                    #print('in if ',item[k],val)
                    while root.left == None:
                        root.left = Node(item[k])
                else:
                    #print('in else ',item[k],val,root.right)
                    while root.right == None:
                        root.right = Node(item[k])
            print('for item ',item)
            # if root:
            #     print(root.data)
            # if root.left:
            #     print(root.left.data)
            # if root.right:
            #     print(root.right.data)
            #     print(root.right.right.data)
            # print("*****END*****")
            # return
            print(self.pre_order_traversal(root))
        return True

    def pre_order_traversal(self, start, traversal=''):
        """root->Left->right"""
        if start:
            traversal += ' ' + str(start.data)
            print(traversal)
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

tree = Binary()
print(tree.generateTrees(3))

"""
Solution
Tree definition

First of all, here is the definition of the TreeNode which we would use.

#Approcah 1 uses recursion - 
First of all let's count how many trees do we have to construct. As you could check in this article, the number of possible BST is actually a Catalan number.

Let's follow the logic from the above article, this time not to count but to actually construct the trees.

Algorithm

Let's pick up number i out of the sequence 1 ..n and use it as the root of the current tree. Then there are i - 1 elements available for the construction of the left subtree and n - i elements available for the right subtree. As we already discussed that results in G(i - 1) different left subtrees and G(n - i) different right subtrees, where G is a Catalan number.

BST

Now let's repeat the step above for the sequence 1 ... i - 1 to construct all left subtrees, and then for the sequence i + 1 ... n to construct all right subtrees.

This way we have a root i and two lists for the possible left and right subtrees. The final step is to loop over both lists to link left and right subtrees to the root.


Complexity analysis

https://leetcode.com/explore/featured/card/recursion-i/253/conclusion/2385/  

class Solution:
    def generateTrees(self, n):
        ""
        :type n: int
        :rtype: List[TreeNode]
        ""
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []


#Using Memoisation

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # record the answer in the process
        memo = {}

        def generateFrom(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            allTrees = []
            for i in range(start, end+1):
                # pick a node as root
                leftTrees = generateFrom(start, i-1)
                rightTrees = generateFrom(i+1, end)
                # construct the subtree
                for j in leftTrees:
                    for k in rightTrees:
                        newRoot = TreeNode(i)
                        newRoot.left = j
                        newRoot.right = k
                        allTrees.append(newRoot)
            memo[(start, end)] = allTrees
            return allTrees
        return generateFrom(1, n) if n else []

Dynamic programming solution
https://leetcode.com/explore/featured/card/recursion-i/253/conclusion/2384/discuss/31521/Python-solution-with-detailed-explanation

"""