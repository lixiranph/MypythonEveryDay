'''
在python中字符串属于不可变对象，不支持原地修改，如果需要修改其中的值，只能创建新的字符串对象。
但是，经常需要原地修改字符串，可以使用io.StringIO对象或者array模块
'''
#例子
import io
s='hello lxr'
sio=io.StringIO(s)
print(id(s))
print(id(sio))
print(sio.getvalue())
sio.seek(7)
sio.write('g')
print(sio.getvalue())