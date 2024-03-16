def f(n: int) -> int:
    if n < 3:
        return n + 1
    elif n >= 3 and n % 2 == 0:
        return n + 2 * f(n + 2)
    elif n >= 3 and n % 2 != 0:
        return f(n - 2) + n - 2


count = 0
for i in range(0, 10000):
    try:
        s = str(f(i))

        if len(s) == 3:
            count += 1

    except:
        continue


print(count)
