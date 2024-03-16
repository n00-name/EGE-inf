def f(n: int) -> int:
    if n < 5:
        return n
    elif n >= 5 and n % 5 == 0:
        return n + f((n / 5) + 1)
    elif n >= 5 and n % 5 != 0:
        return n + f(n + 6)


for i in range(0, 10000):
    try:
        s = f(i)

        if s > 1000:
            print(i)
            break
    except:
        continue