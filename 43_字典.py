'''
字典是键值对，无序，可变序列
'''
a={'name':'LXR','age':'30','job':'programmer'}
print(a.get('age'))
b=dict(name='LXR',age='30',job='programmer')
c=dict([('name','LXR'),('age','30'),('job','programmer')])
print(a)
print(b)
print(c)

k=['name','age','job']
v=['LXR','30','programmer']
d=dict(zip(k,v))
print(d)

x=dict.fromkeys(['name','age','job'])
print(x)