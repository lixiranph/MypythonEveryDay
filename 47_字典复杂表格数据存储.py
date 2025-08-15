r1={'name':'高小一','age':18,'salary':30000,'city':'北京'}
r2={'name':'高小二','age':19,'salary':20000,'city':'北京'}
r3={'name':'高小五','age':20,'salary':10000,'city':'北京'}
tb=[r1,r2,r3]
# xinzi=tb[1].get('salary')
# print(f'{tb[1].get('name')}的薪资是{xinzi}')
#
# for i in range(len(tb)):
#     print(f'{tb[i].get('name')}的薪资是{tb[i].get('salary')}')

for i in range(len(tb)):
    print({tb[i].get('name')},{tb[i].get('age')},{tb[i].get('salary')},{tb[i].get('city')})