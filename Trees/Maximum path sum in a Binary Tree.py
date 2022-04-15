import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


maxi=-1*sys.maxsize
def maxPath(node):
    if node==None:
        return 0
    lh=max(0,maxPath(node.left))
    rh=max(0,maxPath(node.right))
    maxi=max(maxi,lh+rh+node.data)
    # maxi=maxi(maxi,lh+rh)
    return node.data+max(lh,rh)