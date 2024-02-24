x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '131' + s + '1'
    num_2 = '13' + s + '3'

    a = (int(num_1, 15) + int(num_2, 17))
    if a % 11 == 0:
        f = a // 11
        print(f)
