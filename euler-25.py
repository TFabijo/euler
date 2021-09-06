def fibonacci_z_vec_kot_1000_stevkami(a,b):
    c = a + b
    f = [a,b,c]
    while c < 10 ** 999:
        c = c + b
        l = a
        a = b
        b = b + l
        f.append(c)
    return len(f) 

fibonacci_z_vec_kot_1000_stevkami(1,1)
        