'''
python中，'一切都是对象'。实际上，执行def定义函数后，系统就创建了相应的函数对象。
'''
# def print_star(n):
#     print("*"*n)
# print(print_star)
# print(id(print_star))
#
# c=print_star
# print(c)

def test01():
    print('sxtsxt')
test01()
c=test01
print(c)
print(c())
print(id(test01()))
print(id(c()))
print(type(c))