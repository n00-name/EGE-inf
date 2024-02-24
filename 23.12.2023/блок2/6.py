x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '82' + s + '19'
    num_2 = '6' + s + '073'

    a = int(num_1, 15) - int(num_2, 15)
    if a % 11 == 0:
        f = a // 11
        print(f)
