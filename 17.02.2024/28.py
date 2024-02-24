x = '0123456789ABC'
for s in x:
    num_1 = '537' + s + '623'
    num_2 = '6' + s + '35' + s + '2'

    a = int(num_1, 13) - int(num_2, 13)
    if a % 3 == 0:
        print(a)
