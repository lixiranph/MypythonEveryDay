'''
模块介绍
Python 模块(Module),是一个 Python 文件，以.py 结尾,包含了 Python 对象定义和Python语句。
模块让你能够有逻辑地组织你的 Python 代码段。把相关的代码分配到一个模块里能让你的代码更好用，更易懂模块能定义函数，类和变量，模块里也能包含可执行的代码。
模块中有，变量，函数，class面向对象（类-->对象），可执行的代码
使用模块有什么好处？管理方便，容易维护，降低复杂度
'''
PI=3.14
def get_circle_area(r):
    '''
    求圆的面积
    '''
    return PI*r*r
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        '''
        展示学生信息
        :return: None
        '''
        print(f'名字是：{self.name} 年龄是：{self.age}')
print(PI)
print('半径为2的圆的面积是',get_circle_area(2))
stu=Student('alex',30)
stu.show_info()