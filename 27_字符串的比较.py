'''
字符串驻留：仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串驻留池中。Python支持字符串驻留机制，对于符合标识符规则的字符串（仅包含_下划线，字母和数字）
会启动字符串驻留机制
'''
a='abd_33'
b='abd_33'
print(a is b)
c='dd#'
d='dd#'
print(c is d)
print('a' in a)
print('DDD' in a)
print('a' not in a)