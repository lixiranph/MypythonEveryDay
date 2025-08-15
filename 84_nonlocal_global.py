'''
nonlocal用来声明外层的局部变量。
global用来声明全局变量。
【操作】使用 nonlocal 声明外层局部变量
'''
def outer():
    b=10
    def inner():
        nonlocal b #声明外层的局部变量。
        print("inner b:",b)
        b=20
        global a
        a=1000
    inner()
    print("outer b:", b)
outer()
print('a:',a)