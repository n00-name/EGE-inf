
for A in range(1000, 0, -1):
    if all((((x % 36 == 0) and (x % 42 == 0)) <= (x % A == 0) and ( A * (A - 25) < 25 * (A + 200))) == 1 for x in range(0, 1000)):
        print(A)
        break
