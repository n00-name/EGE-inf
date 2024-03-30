
def f(num):
    result = ''
    while num > 0:
        remainder = num % 6
        result = str(remainder) + result
        num //= 6

    return result

count = 0

for num in range(3439, 7410 + 1):

    bin_num = bin(num)[2:]
    c6_num = f(num)

    lst = '0123456789'
    if bin_num[-1] != c6_num[-1]:

        if (num % 9 == 0) or (num % 10 == 0) or (num % 11 == 0):
            count += 1
            print(count, num, bin_num, c6_num)