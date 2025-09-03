'''
属性私有化的问题
1.xx
    一般情况下使用的变量
2._xx
    _PI=3.14
    在某个模块中，如果变量是_xx形式的，使用from import *的方式无法使用
3.__xx
    私有属性/私有方法
    名字重整
    _类名__私有属性名
    _类名__私有方法名
4.__xx__
    主要用于方法
    __init__
    __del__
    __new__
    __str__
5.xx_
    用来区分变量名或者是方法名
'''
# # import TestModule
# from TestModule import *
# # # print(TestModule.PI)
# # print(PI)
# print(_PI)

class Person():
    def __init__(self,name,age):
        self.name=name
        #私有属性
        self.__age=age
    def showInfo(self):
        print(f'name:{self.name},age:{self.__age}')
    def __test(self):
        print(f'我是Person类中的私有方法')
p1=Person('LXR','20')
p1.showInfo()
print(p1.name)
# print(p1.__age)
print(dir(p1))
print(p1._Person__age)
p1._Person__test()