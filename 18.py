#Dane są dwie listy cykliczne powstałe przez zapętlenie listy jednokierunkowej posortowanej
#rosnąco, dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
#Proszę napisać funkcję, która dla dwóch list cyklicznych, usuwa z obu list elementy
#występujące w obu listach. Do funkcji należy przekazać wskaźniki na dwie listy, funkcja
#powinna zwrócić łączną liczbę usuniętych elementów.
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def koniec(p):
    while p.val < p.next.val:
        p = p.next
    return p

def funkcja(p, q):
    p = koniec(p)
    q = koniec(q)
    a = Node(None, p.next)
    b = Node(None, q.next)
    p.next = None
    q.next = None
    cnt = 0
    while a.next is not None and b.next is not None:
        if a.next.val == b.next.val:
            a.next = a.next.next
            b.next = b.next.next
            cnt += 1
        else:
            if a.next.val < b.next.val:
                a = a.next
            else:
                b = b.next
    return cnt
