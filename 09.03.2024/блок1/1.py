s = '5' * 500
count = 0
while ('555' in s) or ('333' in s):
    if '333' in s:
        s = s.replace('333', '5', 1)
    else:
        s = s.replace('555', '3', 1)
        count += 3
print(count)