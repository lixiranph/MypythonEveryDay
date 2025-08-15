'''
单例模式(singleton Pattern)的核心作用是确保一个类只有一个实例，并且提供一个访问该实例的全局访问点。
单例模式只生成一个实例对象,减少了对系统资源的开销。
当一个对象的产生需要比较多的资源，
如读取配置文件、产生其他依赖对象时，
可以产生一个“单例对象”'，
然后永久驻留内存中，从而极大的降低开销。
'''
#测试单例模式
class MysSingleton:
    __obj=None
    __init_flag=True
    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj
    def __init__(self,name):
        if MysSingleton.__init_flag:
            print('initial.....')
            self.name = name
            MysSingleton.__init_flag=False

a=MysSingleton('aa')
b=MysSingleton('bb')
print(a)
print(b)
c=MysSingleton('cc')
print(c)