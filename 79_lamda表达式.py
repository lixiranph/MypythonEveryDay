'''
lambda表达式可以用来声明匿名函数。
lambda 函数是一种简单的、在同一行中定义函数的方法。
lambda函数实际生成了一个函数对象。
lambda表达式只允许包含一个表达式,不能包含复杂语句,该表达式的计算结果就是函数的返回值。
'''

f=lambda a,b,c:a+b+c
print(f)
print(f(2,3,4))
g=[lambda a:a*2,lambda b:b*3,lambda c:c*4]
print (g[0](6),g[1](7),g[2](8))

def test1(a,b,c,d):
    print('#########')
    return a*b*c*d
h=[test1,test1]
print(h[0](2,3,4,5))