'''
编写程序，判断某一个数是否为素数。所谓素数指的是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
'''
a=38
flag=False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
if flag:
    print('是合数')
else:
    print('是素数')
