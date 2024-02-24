from itertools import permutations

# Генерируем все перестановки из цифр 0-9 длиной 7
all_permutations = permutations(range(10), 7)

count = 0

for perm in all_permutations:
    perm_str = ''.join(map(str, perm))

    # Проверяем условия: число делится на 5, все цифры различны, и нет рядом четных и нечетных цифр
    if int(perm_str) % 5 == 0:
        odd_even_valid = all(int(perm_str[i]) % 2 != int(perm_str[i + 1]) % 2 for i in range(len(perm_str) - 1))
        if len(set(perm_str)) == len(perm_str) and odd_even_valid:
            count += 1

print(count)

from itertools import product
k = 0
for i in product('0123456', repeat=7):
    a = ''.join(i)

    if ('22' in a) or ('44' in a) or ('66' in a):
        continue

    if ('11' in a) or ('33' in a) or ('55' in a) or ('77' in a):
        continue

    if a[0] == '0':
        continue

    if len(set(a)) == len(a):
        num = int(a)
        if num % 5 == 0:
            k += 1

print(k)


from itertools import product
k = 0
for i in product('0123456', repeat=7):
    a = ''.join(i)
    if a[0] == '0':
        continue

    #if any(str(num) * 2 in a for num in range(1, 8)):
    #   continue

    #if all(int(a[i]) % 2 != int(a[i + 1]) % 2 for i in range(len(a) - 1)):
    #    continue

    if len(set(a)) != len(a):
        continue

    if int(a) % 5 != 0:
        continue
    odd_even_valid = all(int(a[i]) % 2 != int(a[i + 1]) % 2 for i in range(len(a) - 1))
    if odd_even_valid:
        k += 1
print(k)