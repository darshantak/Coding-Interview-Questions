class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

res=[]
def isLeaf(node):
    if node.left==None and node.right==None:
        return True
    else:
        return False

def addLeft(node):
    curr=node.left
    while curr:
        # s+=1
        # print(s)
        if isLeaf(curr)==False:
            res.append(curr.data)

        if curr.left:
            print(0)
            curr=curr.left
            print(curr.data)
        else:
            print(1)
            curr=curr.right
            # print(curr.data)
        # print(s)

def addRight(node):
    curr=node.right
    temp=[]
    while curr:
        if isLeaf(curr)==False:
            temp.append(curr.data)
        if curr.right:
            curr=curr.right
        else:
            curr=curr.left
    for i in range(len(temp)-1,-1,-1):
        res.append(temp[i])
def addLeaf(node):
    if isLeaf(node)==True:
        res.append(node.data)
    
    if node.left:
        addLeaf(node.left)
    if node.right:
        addLeaf(node.right)

root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.left.left=Node(5)
root.left.right=Node(6)
root.right=Node(7)
root.right.right=Node(8)
root.right.right.left=Node(9)
root.right.right.left.left=Node(10)
root.right.right.left.right=Node(11)
res.append(root.data)
addLeft(root)
addLeaf(root)
addRight(root)
print(res)