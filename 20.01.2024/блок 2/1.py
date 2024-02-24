'''
not - отрицание (2)
and - и (3)
or - или (4)
<= - следование(импликация) (1)
==, != - тождество(антитождество) (1)
'''

print('x y z w f1 f2')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f1 = (w <= y) == (z <= x)
                f2 = (w <= y) and ((not x) == z)
                if f1 == 0:
                    print(x, y, z, w, int(f1), '', int(f2))
