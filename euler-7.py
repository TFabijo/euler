def deli_v_seznamu(n,sez):
    for x in sez:
        if n % x == 0:
            return True
    return False
    


def prastevilo_stevilka_n(n):
    pra = [2]
    stevilo = 2
    i = 1
    while i < n:
        stevilo += 1
        if deli_v_seznamu(stevilo,pra) == False:
            pra.append(stevilo)
            i += 1
        else:
            pass
    return pra[-1]


prastevilo_stevilka_n(10001)

