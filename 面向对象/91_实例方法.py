'''
实例方法
实例方法是从属于实例对象的方法。实例方法的定义格式如下
def 方法名(self[, 形参列表]):
    函数体
方法的调用格式如下
    对象.方法名([实参列表])
要点
1. 定义实例方法时，第一个参数必须为 self。和前面一样，self 指当前的实例对象
2. 调用实例方法时，不需要也不能给 self 传参。self 由解释器自动传参。
函数和方法的区别
1. 都是用来完成一个功能的语句块，本质一样,
2. 方法调用时，通过对象来调用。方法从属于特定实例对象,普通函数没有这个特点。
3. 直观上看，方法定义时需要传递 self,函数不需要
'''
class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_score(self):
        print(f'{self.name}的分数是:{self.score}')
    def print_address(self):
        pass
s2=Student('alex',100)
s2.say_score()
Student.say_score(s2)#实例方法调用的本质
'''
其他操作
1. dir(okj)可以获得对象的所有属性、方法
2. obj._dict_对象的属性字典
3. pass 空语句
4. isinstance(对象,类型)判断“对象”是不是“指定类型
'''
print(dir(s2))
print(Student.__dict__)
print(isinstance(Student.__dict__, dict))
# print(obj._dict_(Student))
print(isinstance(s2,Student))