'''
我们可以通过索引直接访问元素，索引的区间在[0]
'''
a=[10,20,30,40,50,20,70,20,90]
print(a[2])
'''
index()可以获取指定元素首次出现的索引位置
'''
print(a.index(20))
print(a.index(20,3))
'''
count()获得制定元素在列表中出现的次数
'''
print(a.count(20))
'''
len()返回列表的长度
'''
print(len(a))
'''
成员资格判断，判断列表中是否存在指定的元素
'''
print(20 in a)
print(20 not in a)
print(100 not in a)