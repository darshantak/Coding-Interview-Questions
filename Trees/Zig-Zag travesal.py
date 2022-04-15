class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def zigzagLevelOrder(root):
        if root==None:
            return
        q,traversal=[],[]
        flag=0
        q.append(root)
        while len(q)!=0:            
            temp=[]
            for i in range(len(q)):
                node=q.pop(0)
                temp.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
                
            if flag==1:
                traversal.append(temp[::-1])
                flag=0
            else:
                traversal.append(temp)
                flag=1
        return traversal

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)