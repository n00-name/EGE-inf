with open('17-3.txt', 'r') as f:
    nums = f.read().splitlines()
    # nums = list(map(int, f.read().splitlines()))
print(nums)


count = 0
num_chet = 0
num_nechet = 0
min_sred = 100_000

for i in range(0, len(nums) - 1 - 1):

    a = int(nums[i])
    b = int(nums[i + 1])
    c = int(nums[i + 1 + 1])

    if ((abs(a) % 12 == 0) or (abs(b) % 12 == 0) or (abs(c) % 12 == 0)) and ((abs(a) % 3 == 0) and (abs(b) % 3 == 0) and (abs(c) % 3 == 0)):

        count += 1
        # print(a, b, c)

        sred = (a + b + c) / 3
        if min_sred > sred:
            min_sred = sred
            print(min_sred, a, b, c)


print(count, min_sred)