class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def search(node, key):
    if node == None:
        return False
    
    if key == node.data:
        return True
    # elif key == search(node.left):
    #     return True
    # elif key == search(node.right):
    #     return True
   # l = search(node.left,key)
   
    return search(node.left,key) or search(node.right,key)
    
node1=Node(4)
node2=Node(14)
node3=Node(24)
node4=Node(34)
node5=Node(44)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5

print(search(node1, 34))