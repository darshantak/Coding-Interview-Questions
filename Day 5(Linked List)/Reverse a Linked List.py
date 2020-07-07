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

    def print(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    def reverse(self):
        current=self.head
        prev=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
            #why cant i use current.next here in this last current
            
        self.head=prev


ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(32)
ll.print()
print("Reverse is")
ll.reverse()
ll.print()
