'''
for循环通常用于可迭代对象的遍历。
for x in (in后面可以是元组，列表，序列，字符串，字典，迭代器对象（iterator），生成器函数(generator))
'''
# for x in (10,20,30,40,50):
#     print(x*3)
# #遍历字符串中的字符
# for x in list('sxt001'):
#     print(x)
#遍历字典
# d={'name':'lxr','age':'18','address':'鸿博家园',}
# for x in d:
#     print(x)#遍历字典所有的key
#
# for x in d.keys():
#     print(x)  # 遍历字典所有的key
#
# for x in d.values():
#     print(x)  # 遍历字典所有的value
#
# for x in d.items():
#     print(x)  # 遍历字典所有的键值对
#
# for k,v in d.items():
#     print(k)
#     print(v)
'''
range对象
for in range(10)        产生序列：0 1 2 3 4 5 6 7 8 9
for in range(3,10)      产生序列：3 4 5 6 7 8 9
for in range(3,10,2)    产生序列：3 5 7 9
'''
#练习
#利用for循环，计算1-100之间的累加和，偶数加，奇数加

sum=0
sum_even=0
sum_odd=0
for i in range (1,101):
    sum+=i
    if i % 2==0:sum_even+=i
    else :sum_odd+=i
print(f'1-100之间数字的加是：{sum}')
print(f'1-100之间数字的偶数加是：{sum_even}')
print(f'1-100之间数字的奇数加是：{sum_odd}')




