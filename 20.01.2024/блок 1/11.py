from itertools import product
k = 0
for i in product('0123456', repeat=7):
    a = ''.join(i)
    if a[0] == '0' or a[0] == '3' or a[0] == '5':
        continue
    if '22' in a and '44' in a:
        continue
    k += 1
print(k)