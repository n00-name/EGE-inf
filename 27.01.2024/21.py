from itertools import product
count = 0
for num in product('01234567', repeat=10):
    s = ''.join(num)
    if s[0] != '0':
        if s.count('7') == 5:
            if all(pair not in s for pair in '17 71 37 73 57 75 77 77'.split()):
                count += 1

print(count) # 5888