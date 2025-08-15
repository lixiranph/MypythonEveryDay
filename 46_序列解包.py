#序列解包可以用于元组，俩表，字典
x,y,z=(20,30,10)
print(x)
print(y)
print(z)
(a,b,c)=(9,8,10)
print(a)
[a,b,c]=[10,20,30]
print(a)

s={'name':'LXR','age':'30','job':'programmer'}
a,b,c=s
e,d,f=s.values()
h,i,j=s.items()
print(h[1])