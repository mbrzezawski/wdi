class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def print_all(p :Node):
    while p != None:
        print(p.val)
        p = p.next

def create_from_list(T):
    g = Node(None)
    p = g
    for el in T:
        p.next = Node(el)
        p = p.next
    return g.next

def contains(p, num):
    while p != None and p.val < num:
        p = p.next
    return p != None and p.val == num

def wstaw(p, num):
    start = p
    prev = None
    while p != None and p.val < num:
        prev = p
        p = p.next
    if p == None:
        if prev != None:
            prev.next = Node(num)
            return start
        else:
            return Node(num)
    else:
        if p.val == num:
            return start
        else:
            if prev == None:
                return Node(num, p)
            else:
                prev.next = Node(num, p)
                return start

def delete(p, num):
    start = p
    prev = None
    while p != None and p.val < num:
        prev = p
        p = p.next

    if p != None:
        if p.val == num:
            if prev == None:
                return p.next
            else:
                prev.next = prev.next.next
    return start

p = create_from_list([7,14,21])
print(contains(p, 22))
print_all(p)
print("----")
p = delete(p, 21)
print_all(p)

