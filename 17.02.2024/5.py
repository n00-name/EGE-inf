def f(a, x, y):
    return ((x ** 2 - 10 * x + 16) > 0) or ((y ** 2 - 10 * y + 21) > 0) or (x * y < 2 * a)


for a in range(0, 1000):
    if all(f(a, x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break
