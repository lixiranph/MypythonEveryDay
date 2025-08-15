'''
Python支持多重继承，一个子类可以又多个直接父类。这样就具备了多个父类的特点。但是由于，这样会被“类的整体层次搞得非常复杂”尽量避免使用
'''
class A:
    def aa(self):
        print('aa')
class B:
    def bb(self):
        print('bb')
class C(A,B):
    def cc(self):
        print('cc')
c=C()
c.cc()
c.bb()
c.aa()