stevila_do_20 = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
desetice = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]
 
 
def stevila_v_besedi_do_1000(n): 
    c = n % 10 
    b = ((n % 100) - c) / 10  
    a = ((n % 1000) - (b * 10) - c) / 100
    t = "" 
    h = ""
    if n == 1000:
        return "one thousand"
    elif a != 0 and b == 0 and c == 0: 
        t = stevila_do_20[int(a)] + "hundred " 
    elif a != 0: 
        t = stevila_do_20[int(a)] + "hundred and " 
    if b <= 1: 
        h = stevila_do_20[n%100] 
    elif b > 1: 
        h += desetice[int(b)] + stevila_do_20[int(c)] 
    st = t + h 
    return st


def prestej_crke_stevil_do_1000():
    ena_beseda = ""
    for x in range(1,1001):
        ena_beseda += stevila_v_besedi_do_1000(x)
    popravljena_beseda = ena_beseda.replace(" ","")
    return len(popravljena_beseda)

prestej_crke_stevil_do_1000()
 





    