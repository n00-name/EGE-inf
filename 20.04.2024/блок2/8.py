def f(start, end, count):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:

        return f(start + 2, end, count + 1) + f(start + 4, end, count + 1) + f(start + 5, end, count + 1)

for i in range(0, 1500):
    if f(31, i, 0) == 1001:
        print(i)
        break