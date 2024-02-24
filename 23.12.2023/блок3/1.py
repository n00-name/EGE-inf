def f(i, n):
    a = int(str(i), n)
    return a

a = f(64, 16) - f('1E', 16)
b = f(50, 8) + f(36, 8)

print(a, b)