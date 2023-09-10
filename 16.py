#18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
#unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def uniq(p):
    u = Node(None)
    while p is not None:
        temp = p
        cnt = 0
        while temp.next is not None:
            if temp.next.val == p.val:
                cnt += 1
                temp.next = temp.next.next
            else:
                temp = temp.next
        if cnt != 0:
            p = p.next
        else:
            nex = p.next
            p.next = u.next
            u.next = p
            p = nex
    return u.next


def create_linked_list_with_given_elements(L):
    g = Node(None)
    p = g

    for elem in L:
        p.next = Node(elem)
        p = p.next

    return g.next

def print_all(p):
    while p is not None:
        print(p.val)
        p = p.next

p = create_linked_list_with_given_elements([2,3,5,5,3,8,7,8])
p = uniq(p)
print_all(p)