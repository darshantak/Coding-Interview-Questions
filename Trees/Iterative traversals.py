class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
def iterativePreorder(root):
    if root==None:
        return
    st,preorder=[],[]
    st.append(root)
    while len(st)!=0:
        node=st.pop(-1)
        preorder.append(node.data)
        if node.right!=None:
            st.append(node.right)
        if node.left!=None:
            st.append(node.left)
    print(preorder)

def iterativeInorder(node):
    st,inorder=[],[]
    while True:
        if node!=None:
            st.append(node)
            node=node.left
        else:
            if len(st)==0:
                break
            node=st.pop(-1)
            inorder.append(node.data)
            node=node.right

    print(inorder)

def iterativePostorder(node):
    st1,st2=[],[]
    st1.append(node)
    while len(st1)!=0:
        node=st1.pop(-1)
        st2.append(node.data)
        if node.left!=None:
            st1.append(node.left)
        if node.right!=None:
            st1.append(node.right)
    
    print(st2[::-1])


root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)

# iterativePreorder(root)
# iterativeInorder(root)
iterativePostorder(root)