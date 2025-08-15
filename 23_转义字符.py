# '''
# 我们可以使用\+特殊字符，实现某些难以用字符表示的效果。比如换行等。常见的转义字符有这些：
# \(在行尾时) 续行符
# \\反斜杠符号
# \'单引号
# \"双引号
# \b退格(Backspace)
# \n换行横向制表符
# \r回车
# '''
a='I\nlove\nu'
print(a)
b='i \'m a teacher'
print(b)
print('aaabbb\
cccddd')

print('aa'+'bb')
print('aa'*3)

#不换行打印
print('aa',end='')
print('aa',end='##')
print('aa')

myname=input('输入名字')
print(myname)


