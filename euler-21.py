def ambialna_stevila_do_n(n):
    abialna_stevila = set()
    potencialni_abialni_par = {-1:0,0:-1,1:1}
    for x in range(1,n+1):
        delitelji = [1]
        for y in range(2,(x//2)+2):
            if x % y == 0:
                delitelji.append(y)
        if sum(delitelji) > 10000:
            potencialni_abialni_par[x] = 0
        elif sum(delitelji) == x:
            potencialni_abialni_par[x] = 0
        else:
            potencialni_abialni_par[x] = sum(delitelji)
    for x in potencialni_abialni_par:
        if x == potencialni_abialni_par[potencialni_abialni_par[x]]:
            abialna_stevila.add(x)
            abialna_stevila.add(potencialni_abialni_par[x])
        else:
            pass
    return sum(abialna_stevila) + 1

ambialna_stevila_do_n(10000)
        
