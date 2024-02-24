count_1 = 0
for i in range(1000):
    num = bin(i)[2:]

    for _ in range(2):
        if num.count('1') % 2 == 0:
            num += '0'
        else:
            num += '1'

    if 16 <= int(num, 2) <= 32:
        print(i, int(num, 2))
        count_1 += 1


count_2 = 0
for i in range(16, 33):
    count_2 += 1
print(count_2)

ans = count_2  - count_1
print(ans)