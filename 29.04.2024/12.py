def del_(n, m):
    if n % m == 0:
        return 1
    return 0

for A in range(1, 10000):
    flag = True
    for x in range(1, 1001):
        if (((del_(x, 175)) <= (not(del_(x, 25)))) or (2 * x + A >= 1780)) == False:
            flag = False
            break
    if flag:
        print(A)
        break