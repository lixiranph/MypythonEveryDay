while True:
    score=int(input("请输入分数"))
    grade=''
    if score<60:
        grade='不及格'
        print(grade)
        break
    if 80>score>=60:
        grade = '及格'
        print(grade)
        break
    if 90>score>=80:
        grade = '良好'
        print(grade)
        break
    if 100>score>=90:
        grade = '优秀'
        print(grade)
        break
    if score>100 or score<0:
         print('输入不合法')
#
# while True:
#     score=int(input("请输入分数"))
#     grade=''
#     if score<60:
#         grade='不及格'
#         print(grade)
#         break
#     elif 80>score>=60:
#         grade = '及格'
#         print(grade)
#         break
#     elif 90>score>=80:
#         grade = '良好'
#         print(grade)
#         break
#     elif 100>score>=90:
#         grade = '优秀'
#         print(grade)
#         break
#     else:
#         print('输入不合法')

# def getGrade(score: int)-> str | None:
#     if not (0 <= score <= 100):
#         return None
#     if score >= 90:
#         return '优秀'
#     if score >= 80:
#         return '良好'
#     if score >= 60:
#         return '及格'
#     return '不及格'
#
# def main():
#     while True:
#         try:
#             raw = input("请输入分数（0–100）：")
#             score = int(raw)
#         except ValueError:
#             print("❗️ 请输入一个整数！")
#             continue
#
#         grade = getGrade(score)
#         if grade is None:
#             print("❗️ 分数超出范围，请输入 0 到 100 之间的整数。")
#             continue
#
#         print(f"成绩等级：{grade}")
#         break
# if __name__ == '__main__':
#     main()

x=int(input('请输入X坐标'))
y=int(input('请输入Y坐标'))
if (x==0 and y==0):print('原点')
elif (x==0):print('Y轴')
elif (y==0):print('X轴')
elif (x>0 and y>0):print('第一象限')
elif (x<0 and y>0):print('第二象限')
elif (x<0 and y<0):print('第三象限')
else:print('第四象限')