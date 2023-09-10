class Node:
    def __init__(self, inx, value, next=None):
        self.val = value
        self.next = next
        self.inx = inx

def inx_value(p, inx):
    curr = p.next if p.val is None else p
    while curr != None:
        if curr.inx == inx:
            return curr.val
        curr = curr.next

def inx_podstaw_val(p, inx, val):
    curr = p.next if p.val is None else p
    while curr != None:
        if curr.inx == inx:
            curr.val = val
            return curr.val
        curr = curr.next

a = Node(0, 28)
b = Node(2, 54)
c = Node(21, 23)
a.next = b
b.next = c
print(inx_value(a, 22))
print(inx_podstaw_val(a, 2, 53))
