x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
z = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for p in range(9, 36):
    for s1 in x:
        for s2 in y:
            for s3 in z:

                num_1 = s2 + '2' + s2
                num_2 = s2 + '87'
                num_3 = '1' + s1 + s3 + s3

                try:
                    a = int(num_1, p) + int(num_2, p)
                    b = int(num_3, p)
                    if a == b:
                        ans = s1 + s2 + s3
                        ans = int(ans, p)
                        print(ans)
                except ValueError:
                    continue
