class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def preorder(node):
    if node==None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node==None:
        return 
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node):
    if node==None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder(root)
inorder(root)
postorder(root)
#tree looks like
#        1
#       / \
#      2   3
#     / \    
#    4   5    


