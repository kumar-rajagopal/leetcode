from collections import deque
class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def __repr__(self):
        return(dir(self.root.value))
        #return "<Test a:%s b:%s>" % (self.root, self.root.value)

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def print_tree(self, type='pre_order'):
        if type == 'pre_order':
            return (self.pre_order_traversal(self.root, ''))
        elif type == 'in_order':
            return (self.in_order_traversal(self.root, ''))
        elif type == 'post_order':
            return (self.post_order_traversal(self.root, ''))
        elif type == 'level_order':
            return (self.level_order_traversal(self.root, ''))
        else:
            return -1

    def pre_order_traversal(self, start, traversal):
        """root->Left->right"""
        if start:
            traversal += ' ' + str(start.value)
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    def in_order_traversal(self, start, traversal):
        """Left->root->right"""
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += ' ' + str(start.value)
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    def post_order_traversal(self, start, traversal):
        """left->right->root"""
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += ' ' + str(start.value)
        return traversal


    def level_order_traversal(self, root, traversal):
        if root == None:
           return

        current_queue = deque()
        current_queue.append(root)
        current_queue.append(None)

        while len(current_queue) != 0:
            temp = current_queue.popleft()
            #print (str(temp.value) + ",",)

            if temp.left != None:
                current_queue.append(temp.left)

            if temp.right != None:
                current_queue.append(temp.right)

            if current_queue[0] == None:
                print(current_queue.popleft())

                if len(current_queue) != 0:
                    current_queue.append(None)


tree = BinaryTree(7)
tree.root.left = Node(3)
tree.root.right = Node(15)
tree.root.right.left = Node(9)
tree.root.right.right = Node(20)

"""
tree = BinaryTree(3)
tree.root.left = Node(9)
tree.root.right = Node(8)

tree.root.left.left = Node(4)
tree.root.left.right = Node(1)

tree.root.right.left = Node(0)
tree.root.right.right = Node(7)

tree.root.right.left.left = Node(5)
tree.root.right.left.right = Node(2)
r = tree.__repr__()
print("RE ",r)
"""
"""
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2


[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""
print(tree.print_tree('pre_order'))
print(tree.print_tree('in_order'))
print(tree.print_tree('post_order'))
print(tree.print_tree('level_order'))
"""
100
50
25
75
200
125
300

100
50, 200
25, 75, 350

 #pre-order - 100 50 25 75 200 125 300
 #in-order - 25 50 75 100 125 200 300
 #post-order - 25 75 50 125 300 200 100
"""
