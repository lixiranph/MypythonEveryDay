'''
Python 中，除 10 进制，还有其他三种进制
-0b或0B，二进制0 1
-0o或0O，八进制0 1 2 3 4 5 6 7
-0x或0X，十六进制0 1 2 3 4 5 6 7 8 9 a b c d e f
'''
'''
使用int()类型实现转换
'''
int('456')
#int('456abc')

# 会有报错
# Traceback (most recent call last):
#   File "D:\PythonProject\python每日练习\整数.py", line 11, in <module>
#     int('456abc')
#     ~~~^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: '456abc'

a=456.78
print(int(a))

googol=10**1000
print(int(googol))