x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for p in range(9, 36):
    for s1 in x:
        for s2 in y:

            num_1 = '4' + s1 + '46'
            num_2 = s1 + s1 + '17'
            num_3 = s2 + '386' + s2

            try:
                a = int(num_1, p) + int(num_2, p)
                b = int(num_3, p)
                if a == b:
                    ans = s1 + s2 + s1 + s2
                    ans = int(ans, p)
                    print(ans)
            except ValueError:
                continue
