from itertools import permutations

def pandigalni_produkt():
    produkti = set()
    perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
    sez = list(perm)
    for x in sez:
        if x[0] * (x[1] * 1000 + x[2] * 100 + x[3] * 10 + x[4]) == x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8]:
            produkti.add(x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8])
        elif (x[0] * 10 + x[1]) * ( x[2] * 100 + x[3] * 10 + x[4]) == x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8]:
            produkti.add(x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8])
        elif (x[0] * 1000 + x[1] * 100 + x[2] * 10 + x[3]) * x[4] == x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8]:
            produkti.add(x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8])
        elif (x[0] * 100 + x[1] * 10 + x[2]) * (x[3] * 10 + x[4]) == x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8]:
            produkti.add(x[5] * 1000 + x[6] * 100 + x[7] * 10 + x[8])
        else:
            pass
    return sum(produkti)

pandigalni_produkt()

        


