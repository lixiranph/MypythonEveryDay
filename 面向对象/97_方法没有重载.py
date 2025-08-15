'''
方法没有重载
在其他语言中,可以定义多个重名的方法，只要保证方法签名唯一即可。方法签名包含 3个部分:方法名、参数数量、参数类型。
Python中,方法的的参数没有类型(调用时确定参数的类型)，参数的数量也可以由可变参数控制。
因此，Pvthon中是没有方法的重载的。定义一个方法即可有多种调用方式相当于实现了其他语言中的方法的重载。
如果我们在类体中定义了多个重名的方法，只有最后一个方法有效。
建议:不要使用重名的方法!Python 中方法没有重载
'''
# class Person:
#     def say_hi(self):
#         print("Hello")
#     def say_hi(self,name):
#         print(f'{name},hello')
'''
方法的动态性
python是动态语言，我们可以动态的为类添加新的方法，或者动态的修改已有的方法
'''

class Person:
    def work(self):
        print("努力上班")
    def play_game(self):
        print("{0}在玩游戏".format(self))
        print(f'{self}在玩游戏')
    def work2(self):
        print('好好工作，努力上班！赚大钱，娶媳妇儿')
Person.play=Person.play_game
p=Person()
p.work()
p.play_game()
Person.work=Person.work2
p.work2()
