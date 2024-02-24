from itertools import product
k = 0
lst = []
for i in product('КАПКАН', repeat=6):
    a = ''.join(i)

    if a.count('К') == 2 and a.count('А') == 2 and a.count('П') == 1 and a.count('Н') == 1:
        # Так как по две у нас только буквы КК и АА, то проверяем только комбинации с ними
        if ('КК' not in a) and ('АА' not in a):
            lst.append(a)
print(len(set(lst)))
