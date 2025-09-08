#process，子类，进程池
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