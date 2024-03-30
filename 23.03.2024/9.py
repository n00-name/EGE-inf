count = m = 0
with open('17-4.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))
print(nums)

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] - nums[j]) % 2 == 0 and (nums[i] % 31 == 0 or nums[j] % 31 == 0):
            count += 1
            m = max(m, nums[i] + nums[j])
print(count, m)