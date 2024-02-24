num_1 = '12'
num_2 = '33'
num_3 = '406'

for n in range(7, 36):

    a = (int(num_1, n) * int(num_2, n))
    b = int(num_3, n)
    if a == b:
        print(n)
