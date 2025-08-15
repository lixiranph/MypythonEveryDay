'''
object 有一个__str__()方法,用于返回一个对于“对象的描述”,对应于内置函数 str()经常用于 print()方法帮助我们查看对象的信息。__str__()可以重写.
'''
class Person:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f'名字是：{self.name}'
p=Person('lxr')
print(p)


