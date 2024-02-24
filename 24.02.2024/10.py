count = 0

for N in range(300, 401):
    digits = [int(d) for d in str(N)]
    max_num = int(''.join(map(str, sorted(digits, reverse=True))))
    min_num = int(''.join(map(str, sorted(digits))))
    difference = max_num - min_num
    print(N, max_num , min_num, difference)

    if difference == 20:
        count += 1

print(count)

count = 0


count = 0
for i in range(100, 1000):
    n = [int(_) for _ in str(i)]
    n.sort()
    a = str(n[2]) + str(n[1])
    if n[0] != 0:
        b = str(n[0]) + str(n[1])
    elif n[1] != 0:
        b = str(n[1]) + str(n[0])
    else:
        continue
    if int(a) - int(b) == 11:
        count += 1
print(count)