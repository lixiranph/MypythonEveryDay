'''
return 返回值要点
1.如果函数体中包含 return 语句，则结束函数执行并返回值;
2.如果函数体中不包含 return 语句,则返回 None 值。
3.要返回多个返回值,使用列表、元组、字典、集合将多个值“存起来”即可。
'''
def print_star(n):
    print("*"*n)
print_star(5)

def my_avg(a,b):
    return (a+b)/2

c=my_avg(20,30)
print(c)

def add(a,b):
    print(f'计算两个数的和：{a},{b},{a+b}')
    return a+b
c=add(30,40)
print(c)

def test02():
    print('sxt')
    print('lxr')
    return  #return两个作用：1返回值，2结束函数的执行
    print('hello')

d=test02()
print(d)

def test03(x,y,z):
    return [x*10,y*10,z*10]

print(test03(10,20,30))

