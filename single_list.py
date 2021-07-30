class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def print_list(self):
        if self.head is None:
            print("LL is Empty")
        else:
            N = self.head
            while(N is not None):
                print(N.data)
                N=N.next
llist=Linkedlist()
llist.head=Node(1)
second = Node(2)
third = Node(3)
llist.head.next=second
second.next=third
llist.print_list()
        