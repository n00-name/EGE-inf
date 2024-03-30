a = [int(s) for s in open('17-5.txt')]
max13 = max([x for x in a if x%100==13])
b = [sum(a[i:i+3]) for i in range(len(a)-2) if sum([100 <= x < 1000 for x in a[i:i+3]])==2 and sum(a[i:i+3]) <= max13]
print(len(b),max(b))