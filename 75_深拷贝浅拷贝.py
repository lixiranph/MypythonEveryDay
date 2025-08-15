#浅拷贝：不拷贝子对象的内容，只是拷贝子对象的引用
#深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影像源对象
import copy
def testCopy():
    '''
    测试浅拷贝
    '''
    a=[10,20,[5,6]]
    b=copy.copy(a)
    print(f'a:',a)
    print(f'b:',b)
    b.append(30)
    b[2].append(7)
    print('浅拷贝。。。。。。')
    print(f'a:',a)
    print(f'b:',b)
testCopy()
print('--------分隔符--------')
def testCopy1():
    '''
    测试浅拷贝
    '''
    a=[10,20,[5,6]]
    b=copy.deepcopy(a)
    print(f'a:',a)
    print(f'b:',b)
    b.append(30)
    b[2].append(7)
    print('深拷贝。。。。。。')
    print(f'a:',a)
    print(f'b:',b)
testCopy1()