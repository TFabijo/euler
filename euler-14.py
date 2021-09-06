def najdalše_colatzovo_zaporedje_do_n(n):
    krajse_poti = set()
    dolzina_najdalsega = 1
    st_najdalšega = 1
    for x in range(2,n+1):
        st_clenov = 0
        clen = x
        if x in krajse_poti:
            continue
        while clen != 1:
            if clen % 2 == 0:
                clen //= 2
                st_clenov += 1
                krajse_poti.add(clen)
            else:
                clen = 3 * clen + 1
                st_clenov += 1
                krajse_poti.add(clen)
        if st_clenov > dolzina_najdalsega:
            dolzina_najdalsega = st_clenov
            st_najdalšega = x
    return st_najdalšega


najdalše_colatzovo_zaporedje_do_n(1000000)
            

        
