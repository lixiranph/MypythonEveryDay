'''
实例属性
实例属性是从属于实例对象的属性，也称为“实例变量”他的使用有如下几个要点:
1.实例属性一般在 init ()方法中通过如下代码定义:
self.实例属性名 = 初始值
2.在本类的其他实例方法中，也是通过 self 进行访问:self.实例属性名
3.创建实例对象后，通过实例对象访问:
obj01= 类名0)#创建对象，调用 init ()初始化属性obj01.实例属性名 = 值#可以给已有属性赋值，也可以新加属性

实例方法
实例方法是从属于实例对象的方法。实例方法的定义格式如下
def 方法名(self[, 形参列表]):
    函数体
方法的调用格式如下
    对象.方法名([实参列表])
'''

class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_score(self):
        print(f'{self.name}的分数是:{self.score}')

s1=Student('lxr','100')
s1.say_score()

s1.age=32
s1.salary=3000
#del s1
print(s1.salary)

s2=Student('alex','100')
print(s2.name)
