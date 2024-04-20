
lst = []
def f(start: object, end: object, count: object) -> object:
    global lst
    if start == end:
        lst.append(count)
        return 1
    elif start > end:
        return 0
    else:

        return f(start + 1, end, count + 1) + f(start + 2, end, count + 1) + f(start * 2, end, count + 1)

f(1, 28, 0)

minn = min(lst)
ans = lst.count(minn)
print(minn, ans)