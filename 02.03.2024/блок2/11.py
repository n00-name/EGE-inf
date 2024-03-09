x = '0123456789ABCDEF'

for s in x:

    num_1 = s + '1418'
    num_2 = '1' + s + '037'
    num_3 = '2' + s + '209'

    if int(num_1, 13) + int(num_2, 14) == int(num_3, 19):
        print(int(num_1, 13) + int(num_2, 14))

