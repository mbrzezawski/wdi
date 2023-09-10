#Lista zawiera wartości będące liczbami naturalnymi Proszę napisać funkcję repair(p), (p wskazuje
#na pierwszy element listy) która przekształca listę tak aby liczby parzyste znalazły się na końcu listy.
#Funkcja powinna zwrócić wskazanie na przekształconą listę

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def repair(p):
    q = Node(None)
    p = Node(None, p)
    start = p
    while p.next is not None:
        if p.next.val % 2 == 0:
            x = p.next
            p.next = p.next.next
            x.next = q.next
            q.next = x
        else:
            p = p.next
    p.next = q.next
    return start
