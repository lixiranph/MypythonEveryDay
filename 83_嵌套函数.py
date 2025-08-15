'''
测试嵌套函数（内部函数）的定义
一般在什么情况下使用嵌套函数 ?
1.封装-数据隐藏
外部无法访问“嵌套函数”
2.贯彻 DRY(Don't Repeat Yourself)原则
嵌套函数，可以让我们在函数内部避免重复代码。
3. 闭包
后面会详细讲解。
'''
# def outer():
#     print('outer running')
#
#     def inner01():
#         print('inner01 running')
#     inner01()
# outer()

def printChineseName(name,familyName):
    print(familyName,name)

def printEnglishName(name,familyName):
    print(name,familyName)

def printName(isChinses,name,familyName):
    def inner_print(a,b):
        print(a,b)
    if isChinses:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,'熙冉','李')
printName(False,'Xiran','Li')