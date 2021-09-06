def visko_deljiva_trugularna_števila(n):
    stevilo = 1
    tringlarno_stevilo = 1
    d = 0
    while d < n+1:
        stevilo +=1
        tringlarno_stevilo += stevilo
        delitelji = []
        for x in range(1,tringlarno_stevilo + 1):
            if tringlarno_stevilo % x == 0:
                delitelji.append(x)
        d = len(delitelji)
    return tringlarno_stevilo


visko_deljiva_trugularna_števila(500)

