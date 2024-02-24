def f(i, n):
    a = int(str(i), n)
    return a

for i in range(3, 36):
    a = f(121, i) + 1
    b = f(101, 7)
    if a == b:
        print(i)