def je_palindrom(n):
    sez = []
    while n > 0:
        sez.append(n % 10)
        n //= 10 
    return sez == sez[::-1]

def najvecji_palindrom(n=1):
    palindromi = []
    for x in range(100,1000):
        for y in range(x,1000):
            z = x * y
            if je_palindrom(z):
                palindromi.append(z)
    return max(palindromi)

najvecji_palindrom(1)


