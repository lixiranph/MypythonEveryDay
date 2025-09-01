#浅拷贝：不拷贝子对象的内容，只是拷贝子对象的引用
#深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影像源对象
'''
深浅复制:
1.浅复制
copy.copy()2.深复制
copy.deepcopy()
区别与联系:
1.联系
复制出一个新的备份出来
2.区别
对于普通的对象没有区别如果目标对象是复合对象<一个对象的成员变量还是对象>的话，有区别深复制递归复制泼复制，只复制直接对翁
'''
import copy
list1=[1,2,3]
list2=copy.copy(list1)
list3=copy.deepcopy(list1)
print(id(list1))
print(id(list2))
print(id(list3))
print('-'*50)

