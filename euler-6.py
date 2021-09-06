def vsota_kvadratov(n):
    vsota = 0
    for x in range(n+1):
        vsota += x ** 2
    return vsota

def kvadrat_vsote(n):
    vsota = 0
    for x in range(n+1):
        vsota += x
    return vsota ** 2

def razlika(n):
    return - kvadrat_vsote(n) - vsota_kvadratov(n) 

razlika(100)

