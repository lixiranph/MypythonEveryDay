'''
我们把对象比作一个饼干，类就是制造这个饼干的模具
我们通过类定义数据类型的属性（数据）和方法（行为），也就是说'类将行为和状态打包在一起'
'''
class Student:                      #类名首字母一般大写，多个单词采用驼峰原则
    def __init__(self,name,score):  #构造方法一个参数必须为self
        self.name = name            #实例属性
        self.score = score
    def say_score(self):            #实例方法
        print(f'{self.name}的分数是:{self.score}')
s1=Student('李熙冉','100')
s1.say_score()