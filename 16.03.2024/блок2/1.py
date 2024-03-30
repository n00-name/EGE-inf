def f(n: int) -> int:
    if n > 20:
        return n**3 + n
    elif n % 2 == 0:
        return 3 * f(n + 1) + f(n + 3)
    elif n % 2 != 0:
        return f(n + 2) + 2 * f(n + 3)


count = 0
for i in range(0, 1001):
    s = str(f(i))

    if '1' not in s:
        count += 1
print(count)