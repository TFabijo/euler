def različne_potence(a_max,b_max):
    stevila = set()
    for a in range(2,a_max+1):
        for b in range(2,b_max+1):
            stevila.add(a**b)
    return len(stevila)

različne_potence(100,100)

         