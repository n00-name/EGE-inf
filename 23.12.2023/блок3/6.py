x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '55' + s + '36'
    num_2 = s + '2724'

    a = int(num_1, 19) + int(num_2, 19)
    if a % 11 == 0:
        f = a // 11
        print(f)
