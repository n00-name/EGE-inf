import sys

sys.setrecursionlimit(3000)


def f(n: int) -> int:
    if n < 7:
        return 7
    elif n >= 7:
        return n + 1 + f(n - 2)


ans = f(2024) - f(2020)
print(ans)
