x = (2 * (343 ** 123) + 2401) * (3 * (343 ** 137) - 2401)

s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]

print(s.count('6'))
