for num in range(1000, 10000):
    lst = list(map(int, str(num)))

    num_1 = lst[0] + lst[3]
    num_2 = lst[1] + lst[2]

    if num_1 > num_2:
        strnum = str(num_2) + str(num_1)
    else:
        strnum = str(num_1) + str(num_2)

    if strnum == '815':
        print(num)
