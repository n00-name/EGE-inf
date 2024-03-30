def f(n: int) -> int:
    if n > 30:
        return n**2 + 3 * n + 5
    elif n % 2 == 0:
        return 2 * f(n + 1) + f(n + 4)
    elif n % 2 != 0:
        return f(n + 2) + 3 * f(n + 5)


count = 0
for i in range(0, 1001):
    s = str(f(i))

print('asd')