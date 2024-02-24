from itertools import product

count = 1
res = 0
for x in product("ЩОГБА", repeat = 6):
    s = ''.join(x)
    print(count, s)

    if s == 'ОБЩАГА':
        res = count

    count += 1


print(res)