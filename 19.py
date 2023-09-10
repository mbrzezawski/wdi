#Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
#funkcję, która usuwa z listy wejściowej najkrótszą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
#dokładnie jednej najkrótszej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
#Funkcja powinna zwrócić liczbę usuniętych elementów
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def najdluzsza(p):
    p = Node(None, p)
    min_cnt = 1000000
    uniq = False
    min_start = None
    min_end = None
    while p.next != None:
        end_ = p.next
        tmp = 1
        while end_.next != None and end_.val == end_.next.val:
            end_ = end_.next
            tmp += 1
        if tmp < min_cnt:
            min_cnt = tmp
            min_start = p
            min_end = end_
            uniq = True
        elif tmp == min_cnt:
            uniq = False
        p = end_.next
    if uniq == False:
        return 0
    else:
        min_start.next = min_end.next
    return min_cnt


                            