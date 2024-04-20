def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        s_one = start % 10
        s_dec = start // 10
        if s_one != 9:
            s_one += 1
        if s_dec != 9:
            s_dec += 1
        s_new = s_dec * 10 + s_one
        return f(start + 1, end) + f(s_new, end)

print(f(26, 49))