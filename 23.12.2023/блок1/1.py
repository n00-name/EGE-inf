x = 216**6 + 216**4 + 36**6 - 6**14 - 24

s = ''
while x != 0:
    s += str(x % 4)
    x //= 4
s = s[::-1]

# print(s.count("5"))

print(len(set(s)))