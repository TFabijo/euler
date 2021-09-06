def vse_poti(dol,desno):
    if dol == 0 and desno == 0:
        return 0
    elif dol == 0 :
        return 1
    elif desno == 0:
        return 1
    else:
        return vse_poti(dol - 1,desno) + vse_poti(dol,desno - 1) 
#### prpočasi


def fakulteta(n):
    z = 1
    for x in range(1,n+1):
        z *= n
    return z

def binomski_simbol(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n - k) )


def vse_poti_hitrejši(n):
    #ce pogledamo za kvadrat 2x2 in dol ozacimo z D in desno z R lahko zapisemo mozne resitve D1D2R1R2,D1R1D2R2,R1R2D1D2,...
    #vidimo, da v problemu iščemo vse možne kobinacije 
    # vsr resitve dobimo z uporabo binomskega sibola in sicer 2n nad n
    a = 2 * n
    return binomski_simbol(a, n)


vse_poti_hitrejši(20)