def zmozi_sez(sez):
    z = 1
    for x in sez:
        z *= x
    return z

def gcd(x,y):
    while(y):
       x, y = y, x % y
  
    return x


def zanimivi_ulomki():
    stevci = []
    imenovalci = []
    for x in range(1,10):
        for y in range(1,10):
            for z in range(x,10):
                for q in range (1,10):
                    if x * 10 + y == z * 10 + q:
                        break
                    if x == z:
                        if (x * 10 + y)/(z * 10 + q) == y / q:
                            stevci.append(x*10 + y)
                            imenovalci.append(z*10 +q)
                    elif x == q:
                        if (x * 10 + y)/(z * 10 + q) == y / z:
                            stevci.append(x*10 + y)
                            imenovalci.append(z*10 +q)
                    elif y == z:
                        if (x * 10 + y)/(z * 10 + q) == x / q:
                            stevci.append(x*10 + y)
                            imenovalci.append(z*10 +q)
                    elif y == q:
                        if (x * 10 + y)/(z * 10 + q) == x / z:
                            stevci.append(x*10 + y)
                            imenovalci.append(z*10 +q)
                    else:
                        pass
    s = zmozi_sez(stevci)
    i = zmozi_sez(imenovalci)
    while gcd(s,i) != 1:
        d = gcd(s,i)
        s /= d
        i /= d
    return i

zanimivi_ulomki()




                            

