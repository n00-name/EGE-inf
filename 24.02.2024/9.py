for i in range(0, 256):
    num = '{:08b}'.format(i)
    num = num.replace('0', '!')
    num = num.replace('1', ')')

    num = num.replace('!', '1')
    num = num.replace(')', '0')


    dec_num = int(num, 2)

    ans = dec_num - i

    if ans == 99:
        print(i)