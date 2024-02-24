x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '66' + s + '63'
    num_2 = '5' + s + '810'

    a = (int(num_1, 17) - int(num_2, 17))
    if a % 11 == 0:
        f = a // 11
        print(f)
