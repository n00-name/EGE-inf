from itertools import product

count = 0
res = []
for x in product("EКЛОСТ", repeat = 5):
    s = ''.join(x)
    count += 1
    print(count, s)

    if s[0] == 'С' and s.count('ОО') == 1:
        res.append(str(count) + ' ' + s)

print(res)