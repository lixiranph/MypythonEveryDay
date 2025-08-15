'''
一个循环体内可以嵌套另一个循环
'''
# for i in range(5):
#     for j in range(5):
#         print(i, end='\t')
#     print()
'''
利用循环嵌套打印99乘法表
'''

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}', end='\t')
#     print()

r1={'name':'高小一','age':18,'salary':30000,'city':'北京'}
r2={'name':'高小二','age':19,'salary':20000,'city':'上海'}
r3={'name':'高小五','age':20,'salary':10000,'city':'深圳'}
tb=[r1,r2,r3]

for x in tb:
    if x.get('salary') > 15000:
        print(x)