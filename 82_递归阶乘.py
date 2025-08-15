# def factorial(n):
#     if n==1:return 1
#     return n*factorial(n-1)
# for i in range(1,6):
#     print(i,'!=',factorial(i))

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(5)
print(result)
