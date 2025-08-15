'''
一维列表可以帮助我们存储一维，线性的数据
二维列表可以帮助我们存储二维，表格的数据
'''
a=[
    ['lxr','30000','BJ'],
    ['lxr','18000','SH'],
    ['lxr','25000','SZ']
]
for m in range(len(a)):
    for n in range(len(a[m])):
        print(a[m][n],end='\t')
    print()#打印完一行，换行
# print(a[0])
# print((a[0])[0])
# print(a[1])
# print(a[2])