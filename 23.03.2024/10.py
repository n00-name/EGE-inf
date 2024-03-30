file = open('17-1.txt')
arr = [int(_) for _ in file]
count_local_min = 0
max_local_min = -10 ** 5
for i in range(1, len(arr) - 1):
    if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
        count_local_min += 1
        max_local_min = max(max_local_min, arr[i])
print(count_local_min, max_local_min)