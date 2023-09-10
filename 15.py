class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next

def split(p):
    curr = p.next if p.val is None else p

    part = [Node(None) for _ in range(10)]
    lasts = [n for n in part]
    while curr is not None:
        nex = curr.next
        i = curr.val % 10
        lasts[i].next = curr
        lasts[i] = lasts[i].next
        lasts[i].next = None
        curr = nex

    for x in part:
        print_all(x)

    last = lasts[0]
    for i in range(9):
        last.next = part[i + 1].next
        if lasts[i + 1].val is not None:
            last = lasts[i + 1]

    return part[0]




a = Node(3)
b = Node(14)
c = Node(4)
a.next = b
b.next = c

print_all(split(a))