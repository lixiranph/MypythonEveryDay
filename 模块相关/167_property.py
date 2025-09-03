'''
property的使用
    私有属性，提供开放接口，供外界进行访问
'''
class Student():
    def __init__(self,name,age):
        self.__name=name
        #私有属性
        self.__age=age

    def getAge(self):
        return self.__age

    def setAge(self,age):
        if isinstance(age,int):
            self.__age=age
        else:
            raise TypeError('类型错误')
    age=property(getAge,setAge)

stu1=Student('zhangsan',20)
stu1.setAge(17)
# print(stu1.getAge())
stu1.age=18
print(stu1.age)