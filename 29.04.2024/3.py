from itertools import *


def F(x, y, z, w):
    return z <= (x == (w <= y))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, 1, 1, 0), (a2, a3, 0, a4), (0, a5, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in table] == [1, 0, 0]:
                print(p)
                print(''.join(p))