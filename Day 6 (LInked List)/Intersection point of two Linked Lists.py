class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def return_head(self):
        return self.head

#O(n*m) where m is size of ll1 and n is size of ll2
def intersection(ll1,ll2):
    current1=ll1.return_head()
    current2=temp=ll2.return_head()
    while current1:
        # print(current1.data)
        while current2:
            # print(current1.data,current2.data)
            if current1.data==current2.data:
                return current1.data
            else:
                current2=current2.next

        current1=current1.next
        current2=temp

#O(m+n) where m is the size of ll1 and n is the size of ll2
def intersection_optimal(ll1,ll2):
    current1=ll1.return_head()
    current2=ll2.return_head()
    c1,c2=0,0
    while current1:
        c1+=1
        current1=current1.next
    while current2:
        c2+=1
        current2=current2.next
    d=abs(c1-c2)
    current1=ll1.return_head()
    current2=ll2.return_head()
    if c1>c2:
        while d:
            current1=current1.next
            d-=1
    else:
        while d:
            current2=current2.next
            d-=1
    while current1 and current2:
        if current1.data==current2.data:
            return current1.data
        else:
            current1=current1.next
            current2=current2.next


ll1=LinkedList()
ll1.push(0)
ll1.push(32)
ll1.push(5)
ll1.push(6)
ll1.push(7)

ll2=LinkedList()
ll2.push(22)
ll2.push(32)
ll2.push(3)
ll2.push(1)

print(intersection_optimal(ll1,ll2))
