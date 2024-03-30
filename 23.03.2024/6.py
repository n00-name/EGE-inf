with open('17-2.txt', 'r') as f:
    nums = f.read().splitlines()
print(nums)




min_num = 10_001
for num in nums:
    num = int(num)
    if min_num > num:
        min_num = num
print(min_num)

a = 0
for i in range(len(nums)):
    # print(i + 1, int(nums[i]))



    if min_num == int(nums[i]):
        a = i
print(nums.count(str(min_num)), a)