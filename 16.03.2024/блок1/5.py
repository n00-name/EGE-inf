def f(n: int) -> int:
    if n < 3:
        return 2 * n
    elif n >= 3 and n % 2 == 0:
        return 3 * n + 5 + f(n - 2)
    elif n >= 3 and n % 2 != 0:
        return n + 2 * f(n - 6)


print(f(61))
