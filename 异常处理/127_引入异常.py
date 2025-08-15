'''
1. 异常，不正常
2. 案例
    需求：输入被除数与除数，求商，并打印结果
    a,b,c
    问题
    1. str->int如果str不是纯数字的时候，转换出问题
    2. ZeroDivisionError: division by zero
业务核心是求商打印
    1. 使用if-else处理，
    2. 异常处理方案
        try:
        except:
'''
'''
flag=True
while flag==True:
    a=input("输入被除数")
    b=input("输入除数")
    #str->int
    #判断a,b为纯数字
    if a.isdigit() and b.isdigit():
        a=int(a)
        b=int(b)
        #求商
        if b!=0:
            c=a/b
            print(f'商为：{c}')
            flag = False
        else:
            print('操作有误！除数不能为0')
    else:
        print("操作有误！请输入整数")
'''
flag=True
while flag==True:
    a=input("输入被除数")
    b=input("输入除数")
    try:
        a=float(a)
        b=float(b)
        c=a/b
        print(f'商为：{c}')
        flag=False
    except:
        print('操作有误！除数不能为0/请输入整数')