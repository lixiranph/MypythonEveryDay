'''
自定义异常
以及抛出自定义异常

定义一个学生类
私有属性性别
提供对应的设置值，以及访问值的方法
'''
# 自定义异常类
class GenderException(Exception):
    def __init__(self, msg="性别只能设置为 '男' 或 '女'"):
        super().__init__(msg)   # 调用父类构造方法
        self.error_msg = msg
#测试git commit

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.set_gender(gender)  # 使用 setter 确保校验

    # setter
    def set_gender(self, gender):
        if gender in ('男', '女'):
            self.__gender = gender
        else:
            raise GenderException()  # 直接用默认提示

    # getter
    def get_gender(self):
        return self.__gender

    def show_info(self):
        print(f'我叫{self.name}，我是{self.__gender}性')


# 测试
try:
    s1 = Student('alex', '不拿不女')
    s1.show_info()
except GenderException as e:
    print("出错啦:", e)

