'''
使用zip()并行迭代
通过zip()函数对多个序列进行并行迭代，zip()函数在最短序列用完时就会停止
'''
names=('lxr1','lxr2','lxr3','lxr4')
ages=(18,19,29,39)
jobs=('老师','程序员','公务员')

# for name,age,job in zip(names,ages,jobs):
#     print(f'{name},{age},{job}')

for i in range(3):
    print(f'{names[i]},{ages[i]},{jobs[i]}')