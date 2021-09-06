def vsota_stevil_delivih_z_5_in3(n):
    delitelji = []
    for x in range(1,n):
        if x % 5 == 0 or x % 3 == 0:
            delitelji.append(x)
    return sum(delitelji)


vsota_stevil_delivih_z_5_in3(1000)