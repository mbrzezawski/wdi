class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def scal(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p.val <= q.val:
        p.next = scal(p.next, q)
        return p
    else:
        q.next = scal(p, q.next)
        return q

def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next

a = Node(2)
b = Node(7)
c = Node(20)
a.next = b
b.next = c

d = Node(0)
e = Node(5)
f = Node(21)
d.next = e
e.next = f
g = scal(a, d)
print_all(g)



