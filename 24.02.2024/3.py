for i in range(1000):
    num = bin(i)[2:]

    for _ in range(2):
        if num.count('1') % 2 == 0:
            num += '1'
        else:
            num += '0'

    if int(num, 2) > 54:
        print(i, int(num, 2))
        break
