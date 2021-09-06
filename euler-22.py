abeceda = {'A' : 1,'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

def razvrsti_imena_po_abecedi_v_seznam(imena):
    with open (imena,"r",encoding="UTF-8") as dat:
        imen = dat.read()
        sez = imen.split(",")
        sez.sort()
    return sez


razvrsti_imena_po_abecedi_v_seznam("p022_names.txt")

def vsota_imen(imena):
    sez = razvrsti_imena_po_abecedi_v_seznam(imena)
    vsota = 0
    i = 0
    for ime in sez:
        t = ime.replace("\"","")
        i += 1
        vsota_crk = 0
        for crka in t:
            vsota_crk += abeceda[crka]
        vsota += vsota_crk * i
    return vsota


vsota_imen("p022_names.txt")
        
    
