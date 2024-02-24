x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for p in range(9, 36):
    for s1 in x:
        for s2 in y:
            num_1 = '5' + s1 + '16'
            num_2 = s1 + s1 + s1 + '5'
            num_3 = '115' + s2 + s2

            try:
                a = int(num_1, p) + int(num_2, p)
                b = int(num_3, p)
                if a == b:
                    ans = s2 + s1 + s2
                    ans = int(ans, p)
                    print(ans)
            except ValueError:
                continue
