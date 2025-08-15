# num=input('输入一个数字')
# if int(num)<10:
#     print(num)
'''
False,0,0.0,None,空序列对象（空列表，空元祖，空集合，空字典，空字符串，空range对象，空迭代对象）均为False其他为真
'''

if 3:
    print('ok')
a=[]
if not a:
    print('空列表',False)
s='False'
if s:
    print('非空字符串',True)

c=9
if 3<c<20:
    print('3<c<20')
if 3<c and c<20:
    print('3<c and c<20')
if True:
    print('<True>')
else:
    print('<False>')

'''
条件表达式中，不能有复制操作符=
'''
# if 3<c and (c=20):
#     print('赋值符不能出现在条件表达式中')