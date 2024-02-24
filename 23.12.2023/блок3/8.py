x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '12346' + s + '17'
    num_2 = '7' + s + '171'

    a = int(num_1, 17) + int(num_2, 17)
    if a % 16 == 0:
        f = a // 16
        print(f)
