
def vsota_diagonal_spirale_nxn(n):
    najvecje = n * n
    element = 1
    vsota = 1
    korak = 0
    while element != najvecje:
        korak += 2
        for x in range(4):
            element += korak
            vsota += element
    return vsota

