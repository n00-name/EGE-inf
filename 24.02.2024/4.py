for i in range(1000):
    num = bin(i)[2:]

    for _ in range(2):
        if num.count('1') % 2 == 0:
            num += '0'
        else:
            num += '1'

    if int(num, 2) > 96:
        print(i, int(num, 2))
        break