'''
每个对象都有类型，python中最基本的内置数据类型：
1.整形：1，2，3，456 可以+，-，*，/，//（整数除），%取余，**幂
2.浮点型：1.2 1.0
3.布尔型 True False
4.字符串型 我爱你 LXR LS
'''
from traceback import print_tb

a,b=1,2
print(f'a+b={a+b}')
print(f'a-b={a-b}')
print(f'a*b={a*b}')
print(f'a/b={a/b}')
print(f'b%a={b%a}')
print(f'a**1={a**1}')

'''
使用divmod()函数同事得到商和余数
'''
print(f'使用divmod(13,3)函数同时得到商和余数{divmod(13,3)}等于13除以3商为4余数为1，divmod函数返回的是一个元组')
