def F(n):
    if n <= 1:
        return 2
    return F(n - 1) + 5*(n**2)


print(F(39))
