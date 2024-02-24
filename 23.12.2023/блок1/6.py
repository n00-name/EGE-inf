x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '123' + s + '5'
    num_2 = '1' + s + '233'

    if (int(num_1, 15) + int(num_2, 15)) % 14 == 0:
        f = (int(num_1, 15) + int(num_2, 15)) // 14
        print(f)
