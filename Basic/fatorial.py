def fatorial(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

m = int(input('Digite numero :'))
r = fatorial(m)
print(f'O fatorial de {m} é {r}')