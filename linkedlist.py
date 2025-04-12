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
        slow = self
        fast = self
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    

    def middle_node(self):
        slow, fast = self,self
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        return slow.value

        #we use two pointer


head = Node(1)
a = Node(2)
b = Node(4)
c = Node(5)
d = Node(6)

head.next = a
a.next = b
b.next = a
c.next = d
print(head.detect_cycles())
        