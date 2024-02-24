x = 364

for n in range(2, 11):

    s = ''
    while x != 0:
        s += str(x % n)
        x //= n
    s = s[::-1]

    x = 364
    if len(set(s)) == 1:
        print(f'{s} : {n}')

    # print(f'{s} : {n}')