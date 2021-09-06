# pri tem problemu moremo z zvijačo malo zmjšati vsa možna števila, ki ji bomo pregledali za potenciačne rešitve
# recimo vsota stevk 9 pandigalega stevila je 45, ki je deljivo s 3 zato nemore biti prastevilo
# 8 pandigalno stevilo vsota stevk je 36 delivo s 3 nemore biti prastevilo
# 7 pangigalno stevilo vsota stevk je 29 nmoremo nic reci
# se od dolaj navzog
# 1 odpade
#2 pandigalno odpade deljivo s 3
# 3 pandigalno stevilo deljivo s 3
# 4 pandigalno nemoremo nic rec
# 5 pandigalno vsot stevk 15 deljivo s 3 odpade
# 6 pandigalno stevilo vsota stevk je 21 deljivo s 3 odpade
# prastevilo je lahko samo 4 ali 7 pandigalno sevilo
# poskul bom poiskati ce obstaja 7 pandigalno prastevilo

from itertools import permutations

def najvcje_pandigalno_prastevilo():
    stevila = []
    l = list(permutations(range(1, 8)))
    p = []
    for x in l:
        stevilo = 0
        i = 1000000
        for y in x:
            stevilo += y * i
            i //= 10
        p.append(stevilo)
    s = 0
    for pandi in p:
        s += 1
        d = True
        for i in range(2,int(round(pandi ** 0.5,0)) + 1):
            if d == False:
                break
            elif pandi % i == 0:
                d = False
        if d == True:
            stevila.append(pandi)
    return max(stevila)

najvcje_pandigalno_prastevilo()


        

