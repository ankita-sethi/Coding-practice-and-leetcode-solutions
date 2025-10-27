class Node1:
    
    def __init__(self, val):
       self.val = val
       self.left = None
       self.right = None

def invertTree(root):
   if root == None:
       return root
   
   temp= root.left
   root.left=root.right
   root.right=temp

   invertTree(root.left)
   invertTree(root.right)
   return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)
   
node1 =Node1 (12)
node2 = Node1 (3)
node3 = Node1 (5)
node4 = Node1 (23)
node5 = Node1 (9)
node6 = Node1 (7)
node7 = Node1 (4)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.right=node6
node6.right=node7

invertTree(node1)
inOrder(node1)