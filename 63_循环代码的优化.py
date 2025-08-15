'''
1.尽量减少循环内部不必要的计算
2.嵌套循环中，尽量减少内层循环的计算，尽可能往外提
3.局部变量查询较快，尽量使用局部变量
4.连接多个字符串尽量使用join()而不用+
5.列表进行元素插入和删除，尽量在列表尾部操作
'''
#循环代码优化测试
import time
start = time.time()
for i in range(1000):
    result=[]
    for m in range(10000):
        result.append(i*1000+m*100)
end=time.time()
print(f'耗时={end-start}')

strat2=time.time()
for i in range(1000):
    result=[]
    c=i*1000
    for m in range(10000):
        result.append(c+m*1000)
end2=time.time()
print(f'耗时={end2-strat2}')