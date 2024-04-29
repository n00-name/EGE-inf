lst = []

for n in range(2, 1000):
    s = '8' * n

    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)

    lst.append(s)
print(len(set(lst)))