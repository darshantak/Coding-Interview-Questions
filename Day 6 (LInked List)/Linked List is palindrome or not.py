class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def return_head(self):
        return self.head

    def return_tail(self):
        return self.tail

    def reverse(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=slow
        current=slow.next
        slow.next=None
        while current:
            new_node=current.next
            current.next=prev
            prev=current
            current=new_node
        self.tail=prev
        current1=self.head
        current2=self.tail
        while current1 and current2:
            if current1.data==current2.data:
                current1=current1.next
                current2=current2.next
            else:
                return False
        
        return True



ll1=LinkedList()
ll1.push(1)
ll1.push(3)
ll1.push(2)
ll1.push(3)
ll1.push(1)
print(ll1.reverse())

# print(ll1.return_head().next.next.data)