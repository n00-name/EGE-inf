x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for p in range(2, 36):
    for s1 in x:
        for s2 in y:

            num_1 = '103'
            num_2 = '11'
            num_3 = '103'

            try:
                a = int(num_1, p) + int(num_2, 10)
                b = int(num_3, p+1)
                if a == b:
                    print(p)
            except ValueError:
                continue
