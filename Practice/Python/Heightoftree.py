class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def height(node):
    if node == None:
        return -1
    lheight = height(node.left)
    rheight= height(node.right)

    return max(lheight,rheight)+1

node1= Node(12)
node2=Node(23)
node3=Node(14)
node4=Node(6)
node5=Node(8)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5

print("height ", height(node1))