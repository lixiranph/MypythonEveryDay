#process，子类，进程池
'''
multiprocessing.Pool常用函数解析
- apply_async:使用非阻塞方式调用func
- apply(了解即可)使用阻塞方式调用func
- close():关闭Pool，使其不再接受新的任务
- terminate():不管任务是否完成，立即终止
- join():主进程阻塞，等待子进程的退出，必须在close或terminate之后使用;
'''
from multiprocessing import Pool
import time
def work(num):
    print(num)
    time.sleep(1)
if __name__ == '__main__':
    po=Pool()
    for i in range(20):
        po.apply_async(work,args=(i,))
    po.close()
    po.join()