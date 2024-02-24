x = 32**30 + 8**60 - 32

s = ''
while x != 0:
    s += str(x % 4)
    x //= 4
s = s[::-1]

print(s.count('3'))
