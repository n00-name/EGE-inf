def F(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return 2 * F(n - 1)
    elif n > 1 and n % 2 == 1:
        return 5 * n + F(n - 2)


print(F(64))
