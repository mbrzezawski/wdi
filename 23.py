#Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
#pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy) która
#uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu arytmetycznego. Funkcja
#powinna zwrócić liczbę wstawionych elementów.
# 4 - 8 - 12 - 18
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def nwd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def roznica(p):
    r = abs(p.next.val - p.val)
    negative = p.next.val < p.val
    while p.next is not None:
        r = nwd(r, abs(p.next.val - p.val))
        p = p.next
    if negative:
        r *= -1
    return r

def ciag_art(p):
    r = roznica(p)
    start = p
    while p.next is not None:
        if p.next.val - p.val != r:
            x = Node(p.val + r)
            x.next = p.next
            p.next = x
    return start