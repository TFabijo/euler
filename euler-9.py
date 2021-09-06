 
def prava_trojica():
    sez = []
    for c in range(1,1000):
        for x in range(1,1000-c):
            a = x
            b = 1000 - c - x
            sez.append([a,b,c])
    for y in sez:
        if y[0] ** 2 + y[1] ** 2 == y[2] ** 2:
            return y[0] * y[1] * y[2]
        else:
            pass
    return False


poskus()