
for i in range(10, 100):
    num = ''
    num += str(i % 4)
    num += str(i % 2)
    num += str(i % 3)

    if num == '311':
        print(i)
