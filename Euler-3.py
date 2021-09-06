def najvecja_prastevilo(n):
    najvecje_prastevilo = 1
    i = 2
    while i < n / i:  # ker smo n sproti zmajševali z praštevili, ki so manjša od i, mora veljati da i^2 ni vecji od n
            if n % i == 0:
            najvecje_prastevilo = i
            n /= i 
        else:
            i += 1
    if najvecje_prastevilo < n: # v zgornjem postopku nismo privzeli, da je n lahko že praštevilo
        najvecje_prastevilo = n
    return najvecje_prastevilo






      