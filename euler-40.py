def iracionalne():
    st = ""
    for x in range(1,200000):
        st += str(x)
    return int(st[0]) * int(st[9]) * int(st[99]) * int(st[999]) * int(st[9999]) * int(st[99999]) * int(st[999999])

iracionalne()