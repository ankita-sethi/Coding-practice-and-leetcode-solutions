# Define a tree and do traversal - inorder, preorder and postorder
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node): # left root right
    if node == None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def preorder(node): #root left right
    if node== None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)
    
def postorder(node): #left right root
    if node== None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

node1 = Node(12)
node2 = Node(3)
node3 = Node(5)
node4 = Node(23)
node5 = Node(9)
node6 = Node(7)
node7 = Node(4)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.right=node6
node6.right=node7

print("inorder traversal")
inorder(node1)

print("preorder traversal")
preorder(node1)

print("post traversal")
postorder(node1)