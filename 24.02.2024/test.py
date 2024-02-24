
num = 300

lst = list(map(int, str(num)))
lst = set(lst)
print(lst)

max_num = max(lst)
min_num = min(lst)

print(max_num, min_num)

max_num_str = str(max_num) * 2
print(max_num_str)

if min_num == 0:
    lst.remove(0)
    min_num = min(lst)
    min_num_str = str(min_num) + '0'

else:
    min_num_str = str(min_num) * 2

print(min_num_str)

ans = int(max_num_str) - int(min_num_str)
print(ans)
