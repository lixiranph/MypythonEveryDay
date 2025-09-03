'''
- p.start():启动进程，并调用该子进程中的
- p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法
- p.terminate()(了解)强制终止进程p，不会进行任何清理操作
- p.is_alive():如果p仍然运行，返回True.用来判断进程是否还在运行
- p.join([timeout]):主进程等待p终止，timeout是可选的超时时间
- process类常用属性：
    name:当前进程实例别名，默认为Process-N,N为从1开始递增得整数；
    pid:当前进程实例的PID值
'''
"""
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
    p.join()
    print(p.name)
    print(p.pid)
    p1=Process(target=run1,name='process2')
    p1.start()
    p1.join()
    print(p1.name)
    print(p1.pid)
"""
from multiprocessing import Process
#多进程之间的调用是无序的
num=1
def run():
    global num
    num+=5
    print(f'在子进程1中的num={num}')
def run1():
    global num
    num+=10
    print(f'在子进程2中的num={num}')

if __name__ == '__main__':
    print('父进程启动！')
    p1=Process(target=run,name='process1')
    p2=Process(target=run1,name='process2')
    p1.start()
    p1.join()
    p2.start()
    p2.join()
