#kje bo zaustavitveni pogoj??? nekako bomo iskali njavecje potencialno stevilo, katerega vsota stevk na peto je enaka samemu stevilu
#nvazgor bomo ocenili s pomočjo 9
# 9 ** 5 je enako 59046 ki je pet mestno število
# ce bi za stevilo vzeli 99999 bi dobili 295245, ki je šest mestno število, ki bi se ga POTENCIALO dalo zapisat ko vsoto stevk na peto
# ce dodamo se eno devetko torej stevilo 9999999 dobimo sedemestno stevilo, katerega vsota stevk je 7 * 9 ** 5 pa je 413343, ki pa je 6 mestno stevilo
# sepravi nobena kobinacij vsote sedmih števil ne doseze sedem mestega stevila
# sepravi bomo pregledali vsa števil do 6 stevk torej 6 * 9 ** 5 = 354294


def vsota_stevk_na_peto_ki_je_enaka_samemu_stevilu():
    dobra_stevila = []
    for x in range(2,354295):
        vsota = 0
        for y in str(x):
            vsota += int(y) ** 5
        if vsota == x:
            dobra_stevila.append(x)
    return sum(dobra_stevila)

vsota_stevk_na_peto_ki_je_enaka_samemu_stevilu()
