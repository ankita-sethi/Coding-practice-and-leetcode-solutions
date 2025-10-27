#max depth of a tree
class Node1:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    if root == None:
        return 0
    lheight= maxDepth(root.left)
    rheight =maxDepth(root.right)
    return 1+ max(lheight,rheight)

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

print(maxDepth(node1))
