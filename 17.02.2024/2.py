'''
not - отрицание (2)
and - и (3) /\
or - или (4)
<= - следование(импликация) (1)
==, != - тождество(антитождество) (1)
'''

print('x y z w  F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                f = ((x <= z) and (z <= w)) or (y == (x or z))

                if f == 0:
                    print(x, y, z, w, int(f))
