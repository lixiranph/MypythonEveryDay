import random
'''
sort函数修改原列表
'''
a=[20,10,30,40]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
random.shuffle(a)
print(a)

'''
sorted函数返回新列表，不对原列表做修改
'''
b=[20,10,30,40]
print(id(b))
c=sorted(b)
print(sorted(c))

'''
reversed()返回迭代器
'''
a=[20,10,30,40]
c=reversed(a)
print(c)
print(list(c))
'''
max 和 min sum
'''
print(max(a))
print(min(a))
print(sum(a))