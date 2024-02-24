for num in range(1000, 10000):
    lst = list(map(int, str(num)))

    num_1 = lst[0] + lst[1]
    num_2 = lst[2] + lst[3]

    if num_1 > num_2:
        strnum = str(num_1) + str(num_2)
    else:
        strnum = str(num_2) + str(num_1)

    if strnum == '1512':
        print(num)
        break