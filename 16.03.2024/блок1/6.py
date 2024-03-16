def f(n: int) -> int:
    if n > 25:
         return n * n + 2 * n + 1
    elif n <= 25 and n % 2 == 0:
        return 2 * f(n + 1) + f(n + 3)
    elif n <= 25 and n % 2 != 0:
        return f(n + 2) + 3 * f(n + 5)


a = []
for i in range(1, 1001):
    s = str(f(i))
    if '0' not in s:
        a.append(s)
print(len(a))


count = 0
for i in range(1, 1001):
    s = str(f(i))
    if s.count('0') == 0:
        count += 1
print(count)
