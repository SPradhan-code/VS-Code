#Definition of a node in a singly linked list
class Node:
    def __init__(self, data: int):
        self.data=data
        self.next=None
        
#constructor to initialize a new node with data
class Node:
    def __init__(self, new_data : int):
        self.data = new_data
        self.next= None
        head= Node(10)
        head.next = Node(20)
        head.next.next = Node(30)
        head.next.next.next = Node(40)
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

    