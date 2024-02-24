from itertools import product

count = 0
for x in product("EНИСЙ", repeat = 4):
    s = ''.join(x)
    #print(count, s)

    if s[0] != 'Й' and (s.count('E') + s.count('И') >= 1):
        count += 1
        print(count, s)


print(count)
