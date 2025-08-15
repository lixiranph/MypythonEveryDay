'''
序列有字符串，列表，元组，字典，集合
'''
from traceback import print_tb

字符串='lxr'
列表=['lxr',10]
元组=(10,'lxr')
字典={'name':'lxr','age':30}

'''
列表的创建
'''
a=[10,20,'lxr','cyyy']
print(a[0])
a=[]
a.append('lxr')
print(a)

a=list()
a=list('lxr')
print(a)
a=list()
a=list(range(10))
print(a)
a=list('lxr,cyyy')
print(a)

'''
通过range()创建整数列表
range([start,]end[,step])
start参数，表示起始数字，默认0
end参数，表示结束数字
step参数，表示步长默认1
'''
print(list(range(3,15,2)))
print(list(range(15,3,-1)))
print(list(range(3,-10,-1)))

'''
推导式生成列表
'''
a=[x*2 for x in range(5)]
print(a)
a=[x*2 for x in range(100) if x%9==0]
print(a)