'''
多态(polymorphism)是指同一个方法调用由于对象不同可能会产生不同的行为。在现实生活中，我们有很多例子。比如:同样是调用人的休息方法,张三的休息是睡觉,李四的休息是玩游戏，高淇老师是敲代码。同样是吃饭的方法，中国人用筷子吃饭,英国人用刀叉吃饭，印度人用手吃饭。
关于多态要注意以下 2 点
1.多态是方法的多态，属性没有多态,
2.多态的存在有2个必要条件:继承，方法重写
'''

class Man:
    def eat(self):
        print("饿了，吃饭了")
class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")
class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")
class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭")

def manEat(m):
    if isinstance(m, Man):
        m.eat()         #多态，一个方法的调用，可以根据对象的不同调用不同的方法
    else:
        print('不能吃饭')
manEat(Chinese())
manEat(English())
manEat(Indian())