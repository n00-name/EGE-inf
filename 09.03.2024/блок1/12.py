# s = '0' + '1' * 26 + '2' * 54 + '3' * 48 + '0'

for s1 in range(0, 100):
    for s2 in range(0, 100):
        for s3 in range(0, 100):
            s = '0' + '1' * s1 + '2' * s2 + '3' * s3 + '0'


            while not '00' in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '320', 1)
                s = s.replace('03', '3012', 1)

                if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
                    print(s1, s2, s3)
# ans: 6 8 20 