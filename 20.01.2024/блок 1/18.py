x = '0123456789ABCDEFGHIJKLM'
for s in x:
    num_1 = '1' + s + '1' + s + '1' + s + '1' + s + '1'
    num_2 = '20' + s + '24'
    num_3 = '1' + s + '235'

    a = int(num_1, 23) + int(num_2, 23) + int(num_3, 23)
    if a % 22 == 0:
        f = a // 22
        print(f)
