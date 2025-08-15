a='''我是高淇,今年 18 岁了,我在北京尚学堂科技上班。我的儿子叫高洛希，他6岁了。我是一个编程教育的普及者,希望影响 6000 万学习编程的中国人。我儿子现在也开始学习编程，希望他 18 岁的时候可以超过我'''
print(a.startswith('我是'))
print(a.startswith('我是LXR'))
print(a.endswith('超过我'))
print(a.find('高'))
print(a.rfind('高'))
print(a.find('编程'))
print(a.rfind('编程'))
print(a.isalnum())

b='        lxr      '
print(b.strip())
b='*S*X*T'
print(b.strip('*'))
b='*S*X*T**'
print(b.strip('*'))
print(b.rstrip('*'))

'''
大小写转换
'''
a='gaoqi love programming, love SXT'
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())
print(a.swapcase())
a='SXT'
print(a.center(10,'*'))
print(a.center(10))
print(a.ljust(10,'*'))

'''
其他方法
isalnum() 是否为数字或字母
isalpha() 是否只有字母组成（含汉字）
isdigit() 是否只由数字组成
isspace() 检测是否为空白符
isupper() 是否为大写字母
islower() 是否为小写字母
'''