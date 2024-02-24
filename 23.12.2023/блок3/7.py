x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '7' + s + '38596'
    num_2 = '14' + s + '36'
    num_3 = '61' + s + '7'

    a = int(num_1, 23) + int(num_2, 23) + int(num_3, 23)
    if a % 22 == 0:
        f = a // 22
        print(f)
