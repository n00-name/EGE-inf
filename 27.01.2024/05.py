'''
not - отрицание (2)
and - и (3)
or - или (4)
<= - следование(импликация) (1)
==, != - тождество(антитождество) (1)
'''

print('x y z w  F')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):

                f = (not( b <= a)) and (c <= d) or (a and b and c and (not d))
                if f == 1:
                    print(a, b, c, d, int(f))
