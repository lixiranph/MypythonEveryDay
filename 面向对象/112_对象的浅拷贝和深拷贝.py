'''
对象的浅拷贝和深拷贝
·变量的赋值操作
只是形成两个变量，实际还是指向同一个对象。
·浅拷贝
对象包含的子对象内容不拷贝因此，源对象Python 拷贝一般都是浅拷贝。拷贝时和拷贝对象会引用同一个子对象。
·深拷贝
使用 copy 模块的 deepcopy 函数递归拷贝对象中包含的子对象。源对象和拷对象所有的子对象也不同。
'''
import copy
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen

class CPU:
    def calculate(self):
        print('算你姥姥')
        print('CPU对象',self)
class Screen:
    def show(self):
        print('显示一个好看的画面，亮瞎你的钛合金狗眼')
        print('Screen对象',self)
#测试变量赋值
c1=CPU()
c2=c1
print(c1)
print(c2)

#测试浅拷贝
s1=Screen()
m1=MobilePhone(c1,s1)
m2=copy.copy(m1)
print('测试浅拷贝..........')
print(m1,m1.cpu,m1.screen)
print(m2,m2.cpu,m2.screen)

#测试深拷贝
m3=copy.deepcopy(m1)
print('测试深拷贝..........')
print(m1,m1.cpu,m1.screen)
print(m3,m3.cpu,m3.screen)
