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

def levelorder(root):
    if root==None:
        return
    q=[]
    final=[]
    q.append(root)
    while len(q)!=0:
        target=[]
        for i in range(len(q)):
            target.append(q[0].data)
            node=q.pop(0)
            if node.left!=None:
                q.append(node.left)
            if node.right!=None:
                q.append(node.right)
        final.append(target)
    print(final)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# preorder(root)
# inorder(root)
# postorder(root)
levelorder(root)

#tree looks like
#        1
#       / \
#      2   3
#     / \    
#    4   5    


