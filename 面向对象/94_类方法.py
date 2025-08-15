'''
类方法
类方法是从属于“类对象”的方法。类方法通过装饰器@classmethod 来定义，格式如下@classmethod
def 类方法名(cls [,形参列表])函数体
要点如下:
1. @classmethod 必须位于方法上面一行
2.第一个 cls 必须有;cls 指的就是“类对象”本身3.调用类方法格式:“类名.类方法名(参数列表)”。参数列表中，不需要也不能给 cls 传值。
4.类方法中访问实例属性和实例方法会导致错误
5.子类继承父类方法时，传入 cls 是子类对象，而非父类对象
'''
'''
静态方法
Python 中允许定义与“类对象”无关的方法，称为“静态方法”
“静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放到了“类的名字空间里面”，需要通过“类调用”
静态方法通过装饰器@staticmethod 来定义，格式如下@staticmethod
def静态方法名([形参列表])
函数体
要点如下
1. @staticmethod 必须位于方法上面一行
2.调用静态方法格式:“类名.静态方法名(参数列表)”3.静态方法中访问实例属性和实例方法会导致错误
'''
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    company = 'sxt'  # 类属性
    @classmethod
    def printCompany(cls):
        print(cls.company)
        #print(self.name)类方法和静态方法中不能调用实例变量和实例方法
    @staticmethod
    def add(a,b):
        print(f'a+b={a+b}')
        return a+b
Student.printCompany()
class Student2():
    company = 'sxt'  # 类属性
    @staticmethod
    def add(a,b):
        print(f'a+b={a+b}')
        return a+b
Student2.add(1,2)