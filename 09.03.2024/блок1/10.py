for i in range(71, 100):
    f = '1' * i

    while '111' in f:
        f = f.replace('111', '22', 1)
        f = f.replace('222', '11', 1)

    print(f.count('1'), i) # ans: 4 73
