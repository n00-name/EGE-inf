def f(n: int) -> int:
    if n <= 1:
        return 3
    elif n > 1:
        return f(n - 1) + 2 * f(n - 2) - 5


print(f(22))
