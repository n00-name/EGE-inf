for i in range(1000, 10000):
    num = ''
    lst = list(map(int, str(i)))

    strnum_1 = str(lst[0] + lst[1])
    strnum_2 = str(lst[1] + lst[2])
    strnum_3 = str(lst[2] + lst[3])

    num_1 = int(strnum_1)
    num_2 = int(strnum_2)
    num_3 = int(strnum_3)

    min_num = min(num_1, num_2, num_3)

    if min_num == num_1:
        if num_2 > num_3:
            num = strnum_2 + strnum_3
        else:
            num = strnum_3 + strnum_2

    elif min_num == num_2:
        if num_1 > num_3:
            num = strnum_1 + strnum_3
        else:
            num = strnum_3 + strnum_1

    elif min_num == num_3:
        if num_1 > num_2:
            num = strnum_1 + strnum_2
        else:
            num = strnum_2 + strnum_1

    if num == '1414':
        print(i, num)
