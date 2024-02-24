from itertools import product

count = 1
res = 0
for x in product("АВИОРТФ", repeat = 6):
    s = ''.join(x)
    # print(count, s)

    if s[0] != 'О' and s.count('Р') == 2 and count % 2 == 0:
        res += 1
        print(count, s)

    count += 1


print(res)