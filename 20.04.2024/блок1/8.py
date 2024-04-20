def f(start, end, count):
    if start == end and count == 6:
        return 1
    elif start > end or count > 6:
        return 0
    else:

        return f(start+1, end, count + 1) + f(start + 2, end, count + 1) + f(start * 2, end, count + 1)

ans = 0
for i in range(34, 59):
    if f(1, i, 0) != 0:
        ans += 1
print(ans)
