# 227 - 5 = 222
# 222 / 3 = 74

lst = []
def f(start, end, count):
    if start == end:
        global lst
        lst.append(count)
        return 1
    elif start > end or count > 20:
        return 0
    else:

        return f(start+1, end, count + 1) + f(start + 5, end, count + 1) + f(start * 3, end, count + 1)

print(f(1, 74, 0))
print(min(lst) + 2)
