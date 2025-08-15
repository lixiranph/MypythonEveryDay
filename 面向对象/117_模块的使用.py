'''
如何使用模块:
自定义模块
导入模块:
1.import 模块名1,模块名2
导入之后如何使用?
模块名.变量
模块名.函数名(参数)
模块名.类
2.导入模块中相关的数据
from 模块 import 变量，函数，类
如何使用？
直接使用
'''
#第一种方式
import random
ran1=random.randint
print(ran1(1,111111))

#第二种方式
from random import randint
