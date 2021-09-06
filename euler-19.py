meseci = {1:31,2:[28,29],3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def vsi_1_():
    zacetek = 1
    vsi = [1]
    for x in range(1901,2001):
        for mesec in range(1,13):
            if mesec == 2 and x % 400 == 0:
                zacetek += meseci[2][1]
                vsi.append(zacetek)
            elif mesec == 2 and x % 4 == 0:
                zacetek += meseci[2][0]
                vsi.append(zacetek)
            elif mesec == 2:
                zacetek += meseci[2][0]
                vsi.append(zacetek)
            else:
                zacetek += meseci[mesec]
                vsi.append(zacetek)
    return vsi

vsi_1_()


def vse_nedelje():
    ### januarja leta 1901 je bila prava nedelja 6-tega.
    nedelje = 6
    vse_ned = [6]
    while nedelje < 365 * 100:
        nedelje += 7
        vse_ned.append(nedelje)
    return vse_ned 

vse_nedelje()

def stevilo_nedelji_prvega_v_mesecu():
    prvi = vsi_1_()
    nedelje = vse_nedelje()
    st = 0
    for x in prvi:
        if x in nedelje:
            st += 1
        else:
            pass
    return st - 1

stevilo_nedelji_prvega_v_mesecu()


 