'''
object 类是所有类的父类,因此所有的类都有 object 类的属性和方法。我们显然有必要深入研究-下 object 类的结构。对于我们继续深入学习 Python 很有好处。
'''
#通过类的方法mro()和类的属性_mro_可以输出这个类的继承层次结构
class A:
    pass
class B(A):
    pass
class C(B):
    pass
# print(C.mro())

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_age(self):
        print(f'{self.name}的年龄是：{self.age}')
obj=object()
print(dir(obj),end='n')
s2=Person('lxr',30)
print(dir(s2))