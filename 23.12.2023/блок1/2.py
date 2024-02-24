x = (6 * (343**5)) + (5 * (49**7)) - 50

s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]

# print(s.count("5"))

print(s.count("6"))