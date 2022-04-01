class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


x=1
def checkBalance(node):
    global x
    if node==None:
        return 0
    l=checkBalance(node.left)
    r=checkBalance(node.right)
    if abs(l-r)>1:
        x=0
    return 1+max(l,r)

# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.right.left=Node(4)
# root.right.right=Node(5)
# root.right.right.right=Node(6)
root = Node(1)
root.left = Node(2)
# root.right = Node(3)
root.left.left = Node(4)
# root.left.right = Node(5)
checkBalance(root)
print(x)

