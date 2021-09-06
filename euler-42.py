abeceda = {'A' : 1,'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}


def trikotnr_besede(besede_tekst):
    st = 0
    trikotna_stevil =[]
    for x in range(1,100):
        trikotna_stevil.append(int((x*(x+1))/2))
    with open(besede_tekst,"r",encoding="UTF-8") as dat:
        b = dat.read()
        l = b.replace("\"","")
        besede = l.split(",")
    for beseda in besede:
        vsota = 0
        for crka in beseda:
            vsota += abeceda[crka]
        if vsota in trikotna_stevil:
            st += 1
    return st


trikotnr_besede("p042_words.txt")

