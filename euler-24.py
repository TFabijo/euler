from itertools import permutations
def permutacije():
    p = []
    perm = permutations([0,1,2,3,4,5,6,7,8,9])
    for x in perm:
        p.append(x)
    return p[999999]


permutacije()