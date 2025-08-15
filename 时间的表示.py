'''
时间的表示
计算机中时间从1970年1月1日 00：00：00开始,以毫秒进行计算，这个时间觉unix时间点
这个样我们可以用数字来标识所有时间了
'''
import time
print(f'从1970年1月1日 00：00：00到现在已经过了{time.time()}秒了')
b=int(1752224084.4982677)
totalMinutes=b//60
print(f'从1970年1月1日 00：00：00到现在已经过了{totalMinutes}分钟了')
totalHours=totalMinutes//60
print(f'从1970年1月1日 00：00：00到现在已经过了{totalHours}小时了')
totalDays=totalHours//24
print(f'从1970年1月1日 00：00：00到现在已经过了{totalDays}天了')