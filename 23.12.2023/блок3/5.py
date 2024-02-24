x = 9 ** 8 + 3 ** 25 - 14

s = ''
while x != 0:
    s += str(x % 3)
    x //= 3
s = s[::-1]

print(s)

f = sum(map(int,str(s)))

print(f)