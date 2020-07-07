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


def add(ll1,ll2):

    current1=ll1.return_head()
    current2=ll2.return_head()
    carry=0
    ll3=LinkedList()
    while current1 or current2 or carry:
        d1=current1.data if current1 else 0
        d2=current2.data if current2 else 0
        sum=d1+d2+carry
        sum1=sum%10 if sum>=10 else sum
        # print(sum1)
        carry=1 if sum>=10 else 0
        ll3.push(sum1)
        if current1:
            current1=current1.next
        if current2:
            current2=current2.next
    return ll3


ll1=LinkedList()
ll1.push(6)
ll1.push(4)
ll1.push(9)
ll1.push(5)
ll1.push(7)
# # print(ll1.return_head().next.data)


ll2=LinkedList()
ll2.push(4)
ll2.push(8)

ll3=add(ll1,ll2)
ll3.print()