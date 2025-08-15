'''
while,for循环可以附带一个else语句，如果循环没有被break语句结束，则会执行else子句，否则不执行。
'''
#练习
#员工一共4人，录入这4人的薪资，全部录入后，打印提示"您已全部录入4名员工的薪资"最后打印输出录入的薪资和平均薪资
salarySum=0
salarys=[]
for i in range(4):
    s=input('请输入一共4名员工的薪资（输入Q或者q结束）')
    if s.upper() == 'Q':
        print('录入完成，退出')
        break
    if float(s)<0:continue
    salarys.append(float(s))
    salarySum+=float(s)
else:
    print('您已全部录入4名员工的薪资')
print(f'录入薪资为{salarys}')
print(f'平均薪资为{salarySum/4}')