#naloga je podobna nalogi 29
# iscemo zgornjo mejo, do katere bomo pregledovali
# navzgor bomo ocenjevali z 9 ozirom 9! ki znaša 362880
# stevilo 9999999 je yedm mestno stevilo in je vsota fakultet stevk enaka 2540160, ki je tudi 7 mestno stevilo
# stevilo 99999999 je 8 mestno stevilo vsota fakultet pa je 2903040 ,ki pa je 7 mestno stevilo
# to pomeni da vsota fakultet 8 mestega stevil ne more biti nikoli 8 mestno
# zgornja meja pregledovanja bo tako 2540160


def fakulteta(n):
    z = 1
    if n == 0:
        return 1
    for x in range(1,n+1):
        z *= x
    return z

def fakultete_stevk():
    stevila = []
    for x in range(3,2540161):
        s = str(x)
        vsota = 0
        for y in s:
            l = fakulteta(int(y))
            vsota += l
        if x == vsota:
            stevila.append(x)
    return sum(stevila)

fakultete_stevk()



