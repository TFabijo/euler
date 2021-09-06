def  fakulteta(n):
    zmnozek = 1
    for x in range(1,n+1):
        zmnozek *= x
    return zmnozek

def vsota_stevk_fakultete(n):
    fakul = fakulteta(n)
    vsota = 0
    while fakul > 0:
        vsota += fakul % 10
        fakul //= 10
    return vsota

vsota_stevk_fakultete(100)



