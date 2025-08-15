'''
随着编程面临的问题越来越复杂，编程语言本身也在进化，从主要处理简单数据开始数据类型变复杂，进化出了“结构体”;处理数据的方式和随着数据变多进化“数组”逻辑变复杂，进化出了“对象”
1.简单数据
像 30,40，50.4等这些数字，可以看做是简单数据。最初的计算机编程，都是像这样的数字。
2.数组
将同类型的数据放到一起。比如:整数数组[20,30,40]，浮点数数组[10.2,11.3,12.4]，字符串数组:['aa','bb','cc']
'''

'''
3.结构体
将不同类型的数据放到一起，是C语言中的数据结构。比如：
    struct resume{
        int age;
        char name[10];
        double salaryl;
    }
'''
'''
4.对象
将不同类型的数据，方法放到一起就是对象。比如
'''
class Student:
    company='SXT'                   #类属性
    count=0                         #类属性
    def __init__(self,name,score):
        self.name=name              #实例属性
        self.score=score
        Student.count+=1
    def say_score(self):            #实例方法
        print('我的公司是：',Student.company)
        print(self.name,'的分数是：',self.score)
s1=Student('LXR','100')
s1.say_score()
print(Student.count)