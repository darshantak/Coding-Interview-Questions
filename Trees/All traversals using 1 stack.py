class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def traversals(node):
    preorder,postorder,inorder=[],[],[]
    st=[]
    st.append([node,1])
    while len(st)!=0:
        if st[-1][1]==1:
            preorder.append(st[-1][0].data)
            st[-1][1]+=1
            if st[-1][0].left!=None:
                st.append([st[-1][0].left,1])
        elif st[-1][1]==2:
            
            inorder.append(st[-1][0].data)
            st[-1][1]+=1
            if st[-1][0].right!=None:
                st.append([st[-1][0].right,1])
        else:
            postorder.append(st[-1][0].data)
            st.pop(-1)
    print(preorder,postorder,inorder)

root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)
traversals(root)