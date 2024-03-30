with open('4.txt', 'r') as f:
    line = list(map(float, f.read().splitlines()))
print(line)


max_sum = current_sum = line[0]
for i in range(1, len(line)):
    if line[i] < line[i-1]:
        current_sum += line[i]
    else:
        current_sum = line[i]
    max_sum = max(max_sum, current_sum)

print(int(max_sum))
