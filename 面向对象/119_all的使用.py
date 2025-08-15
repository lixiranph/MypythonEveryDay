'''
使用自定义模块的时候：
    1. import模块
    2. from 模块import 变量，类，函数
        from 模块 import *默认导入所有功能
        如果在模块中手动添加全局变量__all__=[]
'''
from myMath import *
result=add(1,2)
print(result)
result=sub(1,2)
print(result)
result=mul(1,2)
print(result)
result=div(1,2)
print(result)
