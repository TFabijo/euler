def eden_iz_sez_deli_n(n,sez):
    for x in sez:
        if n % x == 0:
            return True
    return False


def vsota_praštevil_do_n(n=2000000):
    pra = [2]
    for x in range(3,n):
        if eden_iz_sez_deli_n(x,pra) == False:
            pra.append(x)
    return sum(pra)


vsota_praštevil_do_n()



#def vsota_pra(n=2000000):
    #vsota = 2
    #for x in range(2,n):
        #pra = True
        #for y in range(3,n):
            #if x % y == 0:
                #pra = False
        #if pra:
            #vsota += x
        #return vsota



