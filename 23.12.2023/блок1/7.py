x = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for s in x:
    num_1 = s + '1418'
    num_2 = '1' + s + '037'
    num_3 = '2' + s + '209'

    f = int(num_1, 13) + int(num_2, 14)
    if f == int(num_3, 19):
        print(int(num_3, 19), s)
