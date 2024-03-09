'''
12 * '11' = 24 единиц

122222222 16 + 1

12 * 7 = 84

84 + 17 = 101
'''






# - не верно
from itertools import product
maxx = -1

for i in product('12', repeat=33):
    s = ''.join(i)
    # print(s)
    if s.count('1') == 25 and s.count('2') == 8:

        while '11' in s:
            if '112' in s:
                s = s.replace('112', '5', 1)
            else:
                s = s.replace('11', '7', 1)
        f = sum(map(int, s))
        # print(f)
        maxx = max(maxx, f)
print(maxx)

