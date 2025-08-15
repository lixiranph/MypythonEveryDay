'''
操作：定义一个函数，实现两个数的比较，并返回较大的值
'''
def printMax(a,b):
    '''实现两个数的比较，并返回较大的值'''
    if a > b:print(a,'较大值')
    else:print(b,'较大值')
printMax(10,20)
printMax(30,5)

'''
测试文档字符串的使用
'''
def print_star(n):
    '''根据传入的n，打印多个星号'''
    print("*"*n)
help(printMax)
help(print_star)
help(print_star.__doc__)
help(printMax.__doc__)