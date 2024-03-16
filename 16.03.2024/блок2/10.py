import sys
sys.setrecursionlimit(3001)
def f(n: int) -> int:
    if n >= 3210:
        return 1
    return f(n + 3) + 7


def g(n: int) -> int:
    if n <= 10:
        return n
    return g(n - 3) + 5

print(f(15) - g(3000))