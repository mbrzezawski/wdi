#Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
#liście ułożone są według rosnących potęg. Proszę napisać funkcję
#obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
#są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
#utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
#powinny pozostać niezmienione.
class Node:
    def __init__(self,p ,i , next=None):
        self.p = p
        self.i = i
        self.next = next
def roznica(a, b):
    if b is None:
        return a
    if a is None:
        b.p *= (-1)
        b.next = roznica(a, b.next)
        return b
    if a.i == b.i:
        a.p -= b.p
        a.next = roznica(a.next, b.next)
        return a
    elif a.i < b.i:
        a.next = roznica(a.next, b)
        return a
    else:
        b.p *= (-1)
        b.next = roznica(a, b.next)
        return b

