'''
break语句用于跳出循环，当有嵌套时break只能跳出最近的一层循环
'''
# while True:
#     a=input('请输入一个字符（输入Q或者q结束）')
#     if a.upper() == 'Q':
#         print('循环结束，退出')
#         break
#     else:
#         print(a)

'''
continue语句用于结束本次循环，继续下一次，多个循环嵌套时，continue也时应用于最近的一层循环
'''
#练习
#要求输入员工的薪资，若薪资小于0则重新输入，最后打印出录入员工的数量和工资明细，以及平均薪资
empNum=0
salarySum=0
salarys=[]
while True:
    s=input('请输入员工的薪资（输入Q或者q结束）')
    if s.upper() == 'Q':
        print('录入完成，退出')
        break
    if float(s)<0:continue
    empNum+=1
    salarys.append(float(s))
    salarySum+=float(s)
print(f'员工数为{empNum}')
print(f'录入薪资为{salarys}')
print(f'平均薪资为{salarySum/empNum}')