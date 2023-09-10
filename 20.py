#Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach. Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy (zbiory) z1,z2,z3 w jedną
#listę (zbiór) zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
#wskazanie do listy wynikowej.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def contains(p, num):
        while p is not None and p.val < num:
            p = p.next
        return p is not None and p.val == num

def iloczyn(z1,z2,z3):
    p = Node(None)
    start = p
    while z1 is not None:
        if contains(z2, z1.val) and contains(z3, z1.val):
            p.next = z1
            p = p.next
        z1 = z1.next
    p.next = None
    return start

def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next

a = Node(2)
b = Node(5)
c = Node(20)
a.next = b
b.next = c

d = Node(0)
e = Node(5)
f = Node(21)
d.next = e
e.next = f

g = Node(5)
h = Node(6)
i = Node(21)
g.next = h
h.next = i

print_all(iloczyn(a,d,g))