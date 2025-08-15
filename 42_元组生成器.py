# s=(x*2 for x in range(5))
# print(tuple(s))
# print(list(s))
s=(x*2 for x in range(5))
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())
'''
元组总结
1.元组的核心特点是：不可变序列
2.元组的访问和处理速度比列表快
3.与整数和字符串一样，元组可以作为字典的键，列表则永远不能作为字典的键使用
'''