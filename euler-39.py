def pravokoti_trikotiki():
    najvec_res = 0
    najvec = 0
    for obseg in range(12,1001):
        stevilo_resitev = 0
        for a in range(1,obseg//2 + 1):
            for b in range(a+1,obseg//2 + 2):
                c = obseg - a - b
                if c ** 2 == a ** 2 + b ** 2:
                    stevilo_resitev += 1
        if stevilo_resitev > najvec:
            najvec = stevilo_resitev
            najvec_res = obseg
    return najvec_res

pravokoti_trikotiki()