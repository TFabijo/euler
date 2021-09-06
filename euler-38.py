from itertools import permutations


def pandigitalni_zmozek():
    najvecje = 0
    l = list(permutations(range(1, 10)))
    p = []
    for x in l:
        stevilo = 0
        i = 100000000
        for y in x:
            stevilo += y * i
            i //= 10
        p.append(stevilo)
    for n in range(2,10000):
        st = ""
        for z in range(1,9):
            l = n * z
            if len(st + str(l)) > 9:
                break
            else:
                st += str(l)
        if int(st) in p:
            if int(st) > najvecje:
                najvecje = int(st)
    return najvecje

pandigitalni_zmozek()
            
