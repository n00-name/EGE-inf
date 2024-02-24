from itertools import product
k = 1
for i in product('АКЛОШ', repeat=5):
    a = ''.join(i)

    if a == 'ШКОЛА':
        print(k)
        break
    k += 1
