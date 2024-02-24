def fun(f):
    s = ''
    while f != 0:
        s += str(f % 5)
        f //= 5
    s = s[::-1]
    return s


for x in range(0, 10000):

    f = 4 * (625 ** 1920) + 4 * (125 ** x) - 4 * (25 ** 1940) - 3 * (5 ** 1950) - 1960
    if fun(f).count("0") == 1891:
        print(x)
        break
