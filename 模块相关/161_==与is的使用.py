"""
==
用来比较两个变量的值是否相等
is
用来比较两个变量是否为同一个
基本类型：

引用类型：

"""
import copy
"""
a=10000000
b=10000000
print(a==b)
print(a is b)
print(id(a)==id(b))
"""

list1=[1,2]
list2=[3,4]
list3=[list1,list2]
list4=copy.copy(list3)
list5=copy.deepcopy(list3)
print(list4)
print(list5)
print(id(list3))
print(id(list4))
print(id(list5))

print(list4[0] is list3[0])