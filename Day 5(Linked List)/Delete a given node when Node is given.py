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
    def delete(self,n):
        current=self.head
        if n==1:
            self.head=current.next
            return
        n-=1
        while current and n>1:
            if current is not None:
                current=current.next
            else:
                break
            n-=1
            # print(current.data)
        current.next=current.next.next if current.next else None
    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
            
ll1=LinkedList()
ll1.push(6)
ll1.push(4)
ll1.push(9)
ll1.push(5)
ll1.push(7)
ll1.delete(6)

ll1.print()