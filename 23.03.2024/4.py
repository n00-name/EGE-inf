def f(num):
    result = ''
    while num > 0:
        remainder = num % 6
        result = str(remainder) + result
        num //= 6

    return result

count = 0
for num in range(1000, 10000):

    s = f(num)
    if len(s) <= 5 and (s[-2:] == '13' or s[-2:] == '14'):
        count += 1
        print(count, num, s)
print(count)

