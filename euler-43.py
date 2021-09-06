from itertools import permutations
delitelji = {0:2,1:3,2:5,3:7,4:11,5:13,6:17}

def euler_43():
    stevila = []
    l = list(permutations(range(0, 10)))
    p = []
    for x in l:
        stevilo = 0
        i = 1000000000
        for y in x:
            stevilo += y * i
            i //= 10
        p.append(stevilo)
    for pandi in p:
        pan = str(pandi)
        d = True
        if len(pan) == 9:
            l = pan.zfill(10)
            for y in range(7):
                st = int(l[1+y:y+4])
                if d == False:
                    break
                elif st % delitelji[y] != 0:
                    d = False
            if d == True:
                stevila.append(pandi)
        else:
            for y in range(7):
                st = int(pan[1+y:y+4])
                if d == False:
                    break
                elif st % delitelji[y] != 0:
                    d = False
            if d == True:
                stevila.append(pandi)
    return sum(stevila)


euler_43()

                


