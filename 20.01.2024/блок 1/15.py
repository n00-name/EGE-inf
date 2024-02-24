def check_condition(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    repeated_numbers = [num for num, count in counts.items() if count == 3]

    if len(repeated_numbers) == 2:
        max_number = max(lst, key=int)
        if max_number not in repeated_numbers:
            return 1
    return 0

def test():
    my_list = ['1', '2', '3', '1', '2', '1', '2', '16']

    result = check_condition(my_list)
    print(result)

def main():
    res = 0
    with open('123123.txt') as f:
        for line in f:
            print(line.split())

            l = line.split()

            res += check_condition(l)

    print(res)


def test():
    count = 0
    with open('123123.txt') as f:
        for line in f:
            l = list(map(int, line.split()))

            max_ = max(l)
            s = list(set(l))
            flag = True
            for el in s:
                if l.count(el) not in [1, 3]:
                    flag = False
            if len(s) == 4 and flag and l.count(max_) == 1:
                count += 1
                print(l)
    print(count)

test()