
for x in range(6, 36):
    for y in range(6, 306):

        num_1 = '225'
        num_2 = '405'
        try:
            a = int(num_1, x)
            b = int(num_2, y)
            if a == b:
                print(x)
        except ValueError:
            continue
