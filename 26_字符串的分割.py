import time
a="to be or not to be"
print(a.split())
print(a.split('be'))

a=['sxt','sxt100','sxt200']
print(' '.join(a))
time01=time.time()
a=""
for i in range(100000):
    a+='sxt'
time02=time.time()
print('运算时间'+str(time02-time01))

time03=time.time()
li=[]
for i in range(100000):
    li.append('sxt')

a="".join(li)
time04=time.time()
print('运算时间'+str(time04-time03))