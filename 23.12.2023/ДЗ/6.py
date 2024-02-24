from itertools import *

s = 0
for x in product("АДЖИКА", repeat = 6):
    print(x)
    s += 1

print(s)