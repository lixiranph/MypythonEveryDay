'''
推导式创建序列
推导式是从一个或者多个迭代器快速创建序列的一种方法。
它可以将循环和条件判断结合从而避免冗长的代码。
推导式是典型的 Python 风格，
会使用它代表你已经超过 Python 初学者的水平。
列表推导式生成列表对象，语法如下
[表达式 for item in 可迭代对象]
或者:{表达式 for item in 可迭代对象 if 条件判断}
'''
lst1 = [x for x in range(1, 5)]
lst2 = [x * 2 for x in range(1, 5)]
lst3 = [x*2 for x in range(1,20) if x%5==0]
lst4 = [a for a in 'abcdefg']
cells=[(row,col) for row in range(0,10) for col in range(0,10)]
# print(lst1)
# print(lst2)
# print(lst3)
# print(lst4)
# print(cells)

'''
字典的推导式生成字典对象，格式如下
{key_expression:value_expression for 表达式 in 可迭代对象}
类似于列表推导式，字典推导也可以增加if条件判断、多个 for 循环,
统计文本中字符出现的次数
'''
my_text ='i love you, i love sxt, i love qaogi'
char_count={c:my_text.count(c) for c in my_text}
print(char_count)
'''
集合推导式
集合推导式生成集合，和列表推导式的语法格式类似:
{表达式 for item in 可迭代对象}或者:{表达式 for item in 可迭代对象 if 条件判断)
>>> {x for xin range(1,100) if x%9==0}{99,36, 72,9,45,81, 18,54 90,27, 63}
'''
jihe={x for x in range(1,100) if x%9==0}
list_jihe=list(jihe)
list_jihe.sort()
print(list_jihe)

# jihe = {x for x in range(1, 100) if x % 9 == 0}
# list_jihe = list(jihe)
# list_jihe.sort()          # 就地排序，返回值是 None
# print(list_jihe)          # 直接打印被排序后的列表
'''
很多同学可能会问:“都有推导式，元组有没有?"能不能用小括号呢 ?
>>>(x forx in range(1,100)ifx%9==0)<generator object <genexpr> at 0x0000000002BD3048>
我们发现提示的是“一个生成器对象”。显然，元组是没有推导式的
-个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代发现数据已经没有了
'''
x=(x for x in range(1,100) if x%9==0)
print(x)
gnt=(x for x in range(1,100) if x%9==0)
for x in gnt:
    print(x,end=' ')
    print(x,end=' ')#没有任何输出了