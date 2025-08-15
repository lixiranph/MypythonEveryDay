'''
Python 支持多继承，如果父类中有相同名字的方法，在子类没有指定父类名时,解释器将“从左向右”按顺序搜索
MRO(Method Resolution Order):方法解析顺序。 我们可以通过 mro()方法获得"类的层次结构”，方法解析顺序也是按照这个“类的层次结构”寻找的。
'''
class A:
    def aa(self):
        print('aa')
    def say(self):
        print('say AAA')
class B:
    def bb(self):
        print('bb')
    def say(self):
        print('say BBB')
class C(A,B):
    def cc(self):
        print('cc')
c=C()
print(C.mro())
c.say()
C().say()
