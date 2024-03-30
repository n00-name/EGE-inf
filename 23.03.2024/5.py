"""
with open("17-1.txt", "r") as file1:
    # итерация по строкам
    for line in file1:
        print(line.strip())
"""


with open('17-1.txt', 'r') as f:
    nums = f.read().splitlines()
print(nums)


count = 0
min_num = 10_001
max_num = -10_001
for i in range(0, len(nums) - 1):

    a = int(nums[i])
    b = int(nums[i + 1])
    if (abs(a) % 10 == 6 and abs(a) % 3 == 0) or (abs(b) % 10 == 6 and abs(b) % 3 == 0):
        count += 1

        if max_num < a:
            max_num = a

        if min_num > a:
            min_num = a

print(count, min_num)




