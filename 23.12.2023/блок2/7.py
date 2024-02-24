x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = '9009' + s
    num_2 = '2257' + s

    a = int(num_1, 18) + int(num_2, 18)
    if a % 15 == 0:
        f = a // 15
        print(f)
