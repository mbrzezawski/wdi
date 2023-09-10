#Proszę napisać funkcję Two(p), która otrzymuje wskazanie na listę i rozdziela elementy listy do dwóch
#list. W pierwszej powinny znaleźć się elementy, które w liście wejściowej występowały dokładnie dwa
#razy, a w drugiej wszystkie pozostałe. Funkcja powinna zwrócić wskaźniki do powstałych dwóch list.

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def count(p, num):
    cnt = 0
    while p is not None:
        if p.val == num:
            cnt += 1
        p = p.next
    return cnt

def usun(p, num):
    while p.next is not None:
        if p.next.val == num:
            p.next = p.next.next
        else:
            p = p.next

def Two(p):
    q1 = Node(None)
    q2 = Node(None)
    while p is not None:
        cnt = count(p.next, p.val)
        usun(p, p.val)
        if cnt == 1:
            tmp = p.next
            p.next = q1.next
            q1.next = p
            p = tmp
        else:
            tmp = p.next
            p.next = q2.next
            q2.next = p
            p = tmp
    return q1.next, q2.next
