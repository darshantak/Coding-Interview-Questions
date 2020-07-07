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

    def deleteFromEnd(self,n):
        ptr1=ptr2=self.head
        for i in range(n):
            if ptr2.next==None:
                if i==n-1:
                    self.head=self.head.next
                return self.head
            ptr2=ptr2.next
        
        while ptr2.next:
            ptr2=ptr2.next
            ptr1=ptr1.next

        ptr1.next=ptr1.next.next

    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    
llist=LinkedList()
llist.push(7)  
llist.push(1)  
llist.push(3)  
llist.push(2)  
llist.print()
print("After deleting")
llist.deleteFromEnd(2)
llist.print()
