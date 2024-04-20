def f(start, end, count):
    if start == end and count == 8:
        return 1
    elif start > end or count > 8:
        return 0
    else:

        return f(start + 1, end, count + 1) + f(start + 5, end, count + 1) + f(start * 3, end, count + 1)

ans = 0
for i in range(1000, 1024):
    if f(1, i, 0) != 0:
        ans += 1
print(ans)
