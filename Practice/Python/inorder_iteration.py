class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root): # left root right
    stack1=[]
    stack1.append(root)
    while len(stack1)>0:
        k = stack1[-1]
        if(k.left !=None):
            stack1.append(k.left)
            k.left = None
        else:
            el = stack1.pop()
            print(el.data)
            if(el.right!=None):
                stack1.append(el.right)
                el.right = None
    print('im done')

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.right=node6

print("inorder traversal")
inorder(node1)
