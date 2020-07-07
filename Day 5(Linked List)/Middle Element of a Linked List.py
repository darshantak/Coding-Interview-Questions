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

    def middle_element(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
        # ptr1=ptr2=current=self.head
        # while current.next and current.next.next:
        #     ptr1=current.next
        #     ptr2=current.next.next
        #     current=current.next
        
        # return ptr1.data

ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(4)
ll.push(3)
ll.push(5)
ll.push(0)
ll.push(90)
print(ll.middle_element())