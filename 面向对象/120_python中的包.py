'''
Python中的包
-概念 可以理解为文件夹
    包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境，包中要包含一个__init__.py模块
-新的模块名
    包名.模块名
-包中模块的导入方式
    import package1.module1
    或者
    from package1 import module1
'''
import package1.myMath as myMath
result=myMath.add(10,20)
print(result)
