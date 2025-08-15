'''
package
    模块
    __init__.py
    类中的，__init__初始化方法
    包中的__init__.py初始化模块

    首次使用包中的模块时，__init__.py模块会被执行一次

__init__.py中可以存放什么？
    可以存放同普通模块一样的代码
    变量，类，函数...都是OK的
一般会写一些辅助代码；
    让你更方便的使用模块
    在包的init模块中要导入对应的模块 import模块
    这种方式等价于：在测试文件中使用 import 包.模块
    这种方式等价于：from 包 import *
'''
# import package1
#
# result=package1.myMath.add(10,20)
# print(result)
# from package1.myMath import *
# add(10,20)
#导入模块中的内容
from myMath import *
result=add(10,20)
print(result)