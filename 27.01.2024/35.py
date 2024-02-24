x = '0123456789ABCDE'
for s in x:
    num_1 = '67845' + s + '65'
    num_2 = '1' + s + '23456'

    a = int(num_1, 15) + int(num_2, 15)
    if a % 14 == 0:
        f = a // 14
        print(f)
