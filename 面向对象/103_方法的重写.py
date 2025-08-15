'''
类成员的继承和重写
1. 成员继承:子类继承了父类除构造方法之外的所有成员。
2.方法重写:子类可以重新定义父类中的方法这样就会覆盖父类的方法，也称为“重写
'''
#继承和重写的案例
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
        print(f'我的年龄是的年龄是：{self.__age}')
    def say_introduce(self):
        print(f'我的名字是{self.name}')
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def say_introduce(self):
        '''重写父类方法'''
        print(f'报告老师，我的名字是{self.name}')
s=Student('lxr','30','100')
s.say_age()
s.say_introduce()
