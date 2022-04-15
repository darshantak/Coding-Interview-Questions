class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
maxi=0
def diameter(node):
    global maxi
    if node==None:
        return 0
    lh=1+diameter(node.left)
    rh=1+diameter(node.right)
    maxi=max(maxi,lh+rh-2)
    return max(lh,rh)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.left=Node(4)
root.right.right=Node(6)
root.right.right.left=Node(5)
diameter(root)
print(maxi)