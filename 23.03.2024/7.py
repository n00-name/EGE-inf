with open('17-3.txt', 'r') as f:
    nums = f.read().splitlines()
print(nums)

count = 0
num_chet = 0
num_nechet = 0
max_sum = -100_000

for i in range(0, len(nums) - 1):

    a = int(nums[i])
    b = int(nums[i + 1])

    if ((a + b) % 2 == 1):
        if a % 2 == 0:
            num_chet = a
            num_nechet = b
        elif b % 2 == 0:
            num_chet = b
            num_nechet = a

        if num_chet % 4 == 0 and num_nechet % 11 == 0:
            count += 1

            if max_sum < a + b:
                max_sum = a + b


print(count, max_sum)
