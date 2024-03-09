for i in range(81, 100):
    f = '1' * i

    while '111' in f:
        f = f.replace('111', '2', 1)
        f = f.replace('2222', '1', 1)

    print(f.count('1'), i) # ans: 0 83
