def je_palindrom(n):
    stevilo = str(n)
    return stevilo == stevilo[::-1]

def dvo_bazni_palindromi_do_n(n):
    stevila = []
    deset_bazni_palindromi = []
    for x in range(1,n+1):
        if je_palindrom(x):
            deset_bazni_palindromi.append(x)
    for y in deset_bazni_palindromi:
        binarno = bin(y)
        pravo = binarno[2:]
        if je_palindrom(pravo):
            stevila.append(y)
    return sum(stevila)

dvo_bazni_palindromi_do_n(1000000)



    