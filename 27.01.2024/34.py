x = 4**1503 + 3 * (4**244) - 2 * (4**1444) - 96
s = ''

while x != 0:
    s += str(x % 4)
    x //= 4
s = s[::-1]

summ = 0

for i in s:
    summ += int(i)

print(summ)