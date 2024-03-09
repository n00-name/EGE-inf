s = '1' * 40

for i in range(0, 10):
    f = s + '1' * i

    while '111' in f:
        f = f.replace('111', '2', 1)
        f = f.replace('222', '1', 1)
    print(f, i + 40)
