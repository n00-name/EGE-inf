s = '>' + '1' * 11 + '2' * 12 + '3' * 30

while ('>1' in s) or ('>2' in s) or ('>3' in s):
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)
print(s) # 2222222222222222222222222222222222111111111111111111111111111111>

s = s[:-1]
print(s)
f = sum(map(int, str(s)))
print(f)