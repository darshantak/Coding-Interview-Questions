class Node:
    def __init__(self,data):
        self.left=None
        self.right=None 
        self.data=data
    
def maxDepth(node):
    if node==None:
        return 0
    l=1+maxDepth(node.left)
    r=1+maxDepth(node.right)
    return max(l,r)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.left=Node(4)
root.right.right=Node(6)
root.right.right.left=Node(5)
print(maxDepth(root))