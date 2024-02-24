x = 36 ** 11 + 6 ** 25 - 21
s = ''
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]

print(s.count("5"))