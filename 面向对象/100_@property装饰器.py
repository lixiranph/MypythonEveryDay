'''
@property 装饰器 可以将一个方法的调用方式变成“属性调用”。下面是一个简单的示例，让大家体会一下这种转变
'''
# class Employee:
#     @property
#     def salary(self):
#         return 30000;
#
# emp1=Employee()
# print(emp1.salary)#打印30000
# print(type(emp1.salary)) #打印<class 'int'>
# #emp1.salary()TypeError: 'int' object is not callable
# #emp1.salary=1000#AttributeError: property 'salary' of 'Employee' object has no setter

class Employee1:
    '''
    传统方法
    '''
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,salary):
#         if 1000<=salary<=50000:
#             self.__salary=salary
#         else:
#             print('录入错误，薪水在1000至50000这个范围')
#
#
# emp1=Employee1('lxr',10000)
# print(emp1.get_salary())
# emp1.set_salary(2000)
# print(emp1.get_salary())

class Employee2:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if 1000<=salary<=50000:
            self.__salary=salary
        else:
            print('录入错误，薪水在1000至50000这个范围')

emp2=Employee2('lxr',10000)
print(f'{emp2._Employee2__name}的原工资,{emp2.salary}')
emp2.salary=20000
print(f'{emp2._Employee2__name}的现工资,{emp2.salary}')