'''
继承是面向对象程序设计的重要特征，
也是实现“代码复用”的重要手段。
如果一个新类继承自一个设计好的类,
就直接具备了已有类的特征,
就大大降低了工作难度。
已有的类，我们称为“父类或者基类”，
新的类，我们称为“子类或者派生类”。
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    # @property
    # def age(self):
    #     return self.__age
    # @age.setter
    # def age(self,age):
    #     self.__age=age
    def say_age(self):
        return f'{self.name}的年龄是{self.age}'
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name, age)  #必须显式的调用父类的初始化方法，不然解释器不回去调用
        self.score=score

#Student-->Person-->Object类
print(Student.mro())
s=Student('lxr','30','100')
print(s.name)
print(f'{s.name}的年龄是{s._Person__age}分数是{s.score}')
# s1=Student('zhangsan',24,90)