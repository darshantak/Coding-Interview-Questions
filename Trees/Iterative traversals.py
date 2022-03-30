class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def iterativePreorder(root):
    if root==None:
        return
    q,final=[],[]
    q.append(root)
    while len(q)!=0:
        node=q.pop(-1)
        final.append(node.data)
        if node.right!=None:
            q.append(node.right)
        if node.left!=None:
            q.append(node.left)
    print(final)



root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)

iterativePreorder(root)