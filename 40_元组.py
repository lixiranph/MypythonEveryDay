'''
元组tuple 列表属于可变序列，元组属于不可变序列
元组支持索引访问，切片操作，连接操作，成员关系操作，比较运算操作，计算len,max,min,sum
'''
# a=(10,20,30,40)
# b=tuple([50,60,70,80])
# c=90,
# print(type(a))
# print(type(b))
# print(type(c))
#
# print(a[2])
# print(a[::-1])
# print(sorted(b))

a=[10,20,30]
b=[40,50,60]
c=[70,80,90]
d=zip(a,b,c)
print(list(d))


