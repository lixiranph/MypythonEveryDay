a=100
def f1(n):
    print(f'n:{id(n)}')
    n+=200
    print(f'n:{id(n)}')
    print(n)

f1(a)
print(f'a:{id(a)}')