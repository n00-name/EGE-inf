count = 0
max_num = 0

for i in range(1156, 12210):
    if (i % 2 == 0 or i % 5 == 0) and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 23 != 0:
        count += 1
        max_num = max(max_num, i)

print(count, max_num)