'''
try:

except:

except:

except:
子类在前，父类在后
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
    # except ValueError:
    #     print('操作有误！请输入整数')
    except IOError:
        print('IOerror<UNK>')
    except ZeroDivisionError:
        print('操作有误！除数不能为0')
    except Exception as e:
        print(f'其他异常1,内容为{e}')
    except BaseException as e:
        print(f'其他异常2,内容为{e}')