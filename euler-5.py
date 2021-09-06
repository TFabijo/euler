def zmozi_sez(sez):
    stevilo = 1
    for x in sez:
        stevilo *= x
    return stevilo 


def najmajši_zmonzek(n=20):
    stevila = [2]
    for x in range(3,n+1):
        stevilo = x
        trenuta_stevila = stevila
        for y in trenuta_stevila:
            if stevilo % y == 0:
                stevilo = int(stevilo / y)
        stevila.append(stevilo)
            
    return zmozi_sez(stevila)


najmajši_zmonzek()




        




