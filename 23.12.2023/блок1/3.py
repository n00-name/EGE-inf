x = (5 * (6561**46)) + (5 * (729**15)) - 5 * 5832 - 5

s = ''
while x != 0:
    s += str(x % 9)
    x //= 9
s = s[::-1]

print(s.count("4"))