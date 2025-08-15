'''
标准格式为：[起始偏移量 start:终止偏移量 end[:步长 step]] 注：当步长省略时顺便可以省略第二个冒号
'''

#提取整个列表
a=[10,20,30,40,50,60]
print(a[:])
print(a[1:3:1])
print(a[1::2])
print(a[1:])
print(a[:2])
print(a[-3:])
print(a[::-1])
print(a[-5:-3])