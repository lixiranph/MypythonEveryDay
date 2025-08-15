'''
类对象
我们在前面讲的类定义格式中，“class 类名:实际上，当解释器执行 class 语句时就会创建一个类对象。
【操作】测试类对象的生成
'''
class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def say_score(self):
        print(f'{self.name}的分数是:{self.score}')
print(type(Student))
print(id(Student))

stu2=Student
s1=Student('lxr',100)
s2=stu2('alex','100')
s1.say_score()
s2.say_score()
