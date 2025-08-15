'''
Python 对于类的成员没有严格的访问控制限制，这与其他面向对象语言有区别。关于私有属性和私有方法，有如下要点:
1.通常我们约定，两个下划线开头的属性是私有的(private)。其他为公共的(public),
2.类内部可以访问私有属性(方法)
3.类外部不能直接访问私有属性(方法)
4.类外部可以通过 “_类名__私有属性(方法)名”访问私有属性(方法)
【注】方法本质上也是属性!只不过是可以通过()执行而已。所以，此处讲的私有属性和公有属性，也同时讲解了私有方法和公有方法的用法。如下测试中,同时也包含了私有方法和公有方法的例子。
'''
class Employee:
    __company='百战程序员'
    def __init__(self,name,age):    #私有属性
        self.name=name
        self.__age=age
    def __work(self):               #私有方法
        print('好好工作，努力上班！赚大钱，娶媳妇儿')
        print(f'年龄是{self.__age}')
        print(Employee.__company)

e=Employee('LXR',30)
print(e.name)
print(e._Employee__age)
print(dir(e))
e._Employee__work()
print(Employee._Employee__company)
