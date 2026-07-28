from typing import Any, Optional

class Node:
    def __init__(self, new_data: Any):
        self.data = new_data
        self.next: Optional["Node"] = None 
def traversaList(head: Optional[Node]) -> None:
    while head is not None :
        print(head.data, end=" ")
        if head.next is not None:
            print("->",end="")
        head=head.next
    print()
if __name__ == "__main__":
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    head.next.next.next=Node(40)
    traversaList(head)