# num=0
# while num<=10:
#     print(num)
#     num+=1

#计算1-100之间数字的累加,以及偶数加和奇数加
num=0
sum=0
sum_even=0
sum_odd=0
while num<=100:
    sum+=num
    if num%2==0:sum_even+=num
    else:sum_odd+=num
    num+=1
print(f'1-100之间数字的加是：{sum}')
print(f'1-100之间数字的偶数加是：{sum_even}')
print(f'1-100之间数字的奇数加是：{sum_odd}')
