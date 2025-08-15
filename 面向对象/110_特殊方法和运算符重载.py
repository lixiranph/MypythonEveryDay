a=20
b=30
c=a+b
d=a.__add__(b)
print(f'c={c}')
print(f'd={d}')
'''
运算符的重载
'''
class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'名字是{self.name}'
    def __add__(self, other):
        if isinstance(other, Person):
            return f'{self.name}--{other.name}'
        else:
            return '不是同类对象不能相加'
    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return '不是同类对象不能相加'
p1=Person('Alex')
p2=Person('Lrq')
x=p1+p2
print(x)
print(p1*3)