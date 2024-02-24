
def f(a, x, y):
    return (4 * x + y < a) or (x < y) or (22 <= x)

for a in range(0, 1000):
    if all(f(a, x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break

for a in range(0, 1000):
    if all( ((4 * x + y < a) or (x < y) or (22 <= x)) == 1 for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break