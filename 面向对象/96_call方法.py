'''
call方法和可调用对象
定义了 call 方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用，
'''
# a,b=30,50
# c=a+b
# d=a.__add__(b)
# print(c)
# print(d)
class SalaryAccount():
    '''
    工资计算类
    '''
    def __call__(self,salary):
        print('算工资啦')
        yearSalary = salary*12
        daySalary=salary/22.5
        hourSalary=daySalary/8
        return dict(yearSalary = yearSalary, monthSalary = salary, daySalary = daySalary, hourSalary = hourSalary)
        # return {
        #     'yearSalary': yearSalary,
        #     'monthSalary': salary,
        #     'daySalary': daySalary,
        #     'hourSalary': hourSalary
        # }
if __name__ == '__main__':
    s=SalaryAccount()
    print(s(30000))
