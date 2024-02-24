x = 64**150 + 4**300 - 32

s = ''
while x != 0:
    s += str(x % 8)
    x //= 8
s = s[::-1]

print(s.count('7'))