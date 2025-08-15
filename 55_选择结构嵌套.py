'''
选择结构嵌套
控制好缩进量
'''
# score=int(input("请输入分数"))
# if score>100 or score<0:
#     print("请输入一个0-100之间分数")
# else:
#     if score>=90:
#         grade='A'
#         print(grade)
#     elif score>=80:
#         grade = 'B'
#         print(grade)
#     elif score>=70:
#         grade = 'C'
#         print(grade)
#     elif score>=60:
#         grade = 'D'
#         print(grade)
#     elif score == 100:
#         grade = '满分'
#         print(grade)
#     else:
#         grade = 'E'
#         print(grade)
#     print(f'分数是{score},等级为{grade}')

'''
另一种写法
'''
score=int(input("请输入分数"))
degree='ABCDE'
num=0
if score>100 or score<0:
    print("请输入一个0-100之间分数")
else:
    num=score//10
    if num<6:
        num=5
    print(degree[9-num])
print(f'分数是{score},等级为{degree[9-num]}')