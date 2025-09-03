'''
程序：是一个指令的集合
进程：正在执行的程序
多进程
- 程序开始运行时，首先会创建一个主进程
- 在主进程（父进程）下，我们可以创建新的（子进程），子进程依赖于主进程，如果主进程结束，程序会退出
- python提供了非常好用的多进程包multiprocessing,借助这个包，可以轻松完成从单进程到并发执行的转换
- process(target，name,args)
    - target表示调用对象，即子进程要执行的任务
    - args表示调用对象的位置参数元组，args=(1,)
    - name为子进程的名称
'''
from multiprocessing import Process
def run(name):
    print(f'hello{name}')
def run1():
    print('hello123')
'''
在多进程的条件先需要if __name__=='__main__':
'''
if __name__ == '__main__':
    p=Process(target=run,args=('test',),name='process1')
    p.start()
    p.join(5)
    print(p.name)
    p1=Process(target=run1,name='process2')
    p1.start()
    p1.join()
    print(p1.name)