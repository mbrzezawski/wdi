class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def reverse(p):
    if p.next is None:
        return p
    else:
        prev = reverse(p.next)
        q = prev
        while q.next != None:
            q = q.next
        q.next = p
        p.next = None
        return prev

def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next

a = Node(2)
b = Node(7)
c = Node(20)
a.next = b
b.next = c
print_all(reverse(a))
