def f(n: int) -> int:
    if n > 30:
        return n * n + 5 * n + 4
    elif n <= 30 and n % 2 == 0:
        return f(n + 1) + 3 * f(n + 4)
    elif n <= 30 and n % 2 != 0:
        return 2 * f(n + 2) + f(n + 5)


count = 0
for i in range(1, 1001):
    s = str(f(i))
    suma = sum(map(int, s))
    if suma == 27:
        count += 1

print(count)
