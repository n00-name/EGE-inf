x = (4 ** 4) * (5 ** 69) - 70

s = ''
while x != 0:
    s += str(x % 5)
    x //= 5
s = s[::-1]

print(s.count('0'))
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))
print(s.count('4'))
