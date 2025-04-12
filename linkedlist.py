class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        while curr:
            print(curr.value)
            curr = curr.next

    def detect_cycles(self):
        #we use two pointer


head = Node(1)
a = Node(2)
b = Node(4)
c = Node(5)

head.next = a
a.next = b
b.next = c

print(head)
        