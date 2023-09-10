#Dwie listy zawieraj¡ niepowtarzaj¡ce si¦ (w obr¦bie listy) liczby naturalne. W obu listach liczby s¡ posortowane rosn¡co. Prosz¦ napisa¢ funkcj¦ usuwaj¡c¡ z ka»dej listy liczby wyst¦puj¡ce w drugiej. Do funkcji
#nale»y przekaza¢ wskazania na obie listy, funkcja powinna zwróci¢ ª¡czn¡ list¦ usuni¦tych elementów.

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def funkcja(p, q):
    p = Node(None, p)
    q = Node(None, q)
    cnt = 0
    while p.next != None and q.next != None:
        if p.next.val == q.next.val:
            p.next = p.next.next
            q.next = q.next.next
            cnt += 1
        else:
            if p.next.val < q.next.val:
                p = p.next
            else:
                q = q.next
    return cnt

