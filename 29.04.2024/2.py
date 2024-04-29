from itertools import *


def F(x, y, z, w):
    return ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, a1, 1, 1), (a2, 0, 0, 0), (a3, a4, 0, a5)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
                print(''.join(p))