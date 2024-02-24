x = 8**511 - 4**511 + 2**511 - 511

s = ''
while x != 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]

print(s.count('0'))