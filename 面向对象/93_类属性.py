'''
类属性
类属性是从属于“类对象"的属性,也称为"类变量"。由于,类属性从属于类对象，可以被所有实例对象共享。
类属性的定义方式
class 类名:
类变量名=初始值
在类中或者类的外面，我们可以通过:"类名.类变量名"来读写。
'''
class Student:
    company='sxt'   #类属性
    count=0         #类属性
    def __init__(self,name,score):  #实例属性
        self.name=name
        self.score=score
        Student.count+=1

    def say_score(self):             #实例方法
        print(f'{self.name}的公司是{Student.company}')
        print(f'{self.name}的分数是{self.score}')
s1=Student('lxr','100')
s2=Student('alex','100')
s1.say_score()
s2.say_score()
print(f'一共创建了{Student.count}个Student对象')

