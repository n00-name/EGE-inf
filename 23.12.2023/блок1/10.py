x = '0123456789ABCDE'
y = '0123456789ABCDEFG'
for s1 in x:
    for s2 in y:

        num_1 = '123' + s1 + '5'
        num_2 = '67' + s2 + '9'

        a = (int(num_1, 15) + int(num_2, 17))
        if a % 131 == 0:
            f = a // 131
            print(f)
