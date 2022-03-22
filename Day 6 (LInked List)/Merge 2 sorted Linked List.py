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

    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def insertafter(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

def merge(ll1,ll2):
    current1=ll1.return_head()
    current2=ll2.return_head()
    ll3=LinkedList()
    while current1 and current2:
        if current1.data<=current2.data:
            ll3.insertafter(current1.data)
            current1=current1.next
        else:
            ll3.insertafter(current2.data)
            current2=current2.next
    while current1:
        ll3.insertafter(current1.data)
        current1=current1.next
    
    while current2:
        ll3.insertafter(current2.data)
        current2=current2.next
    
    return ll3


ll1=LinkedList()
ll1.push(8)
ll1.push(6)
ll1.push(2)
# ll1.print()
# print(ll1.return_head().next.data)

ll2=LinkedList()
ll2.push(10)
ll2.push(9)
ll2.push(7)

ll3=merge(ll1,ll2)
current=ll3.return_head()
while current:
    print(current.data)
    current=current.next
