import multiprocessing
import time
# def test():
#     n=5
#     while n>0:
#         print(n)
#         time.sleep(1)
#         n-=1
# if __name__ == '__main__':
#     p=multiprocessing.Process(target=test)
#     p.start();
#     p.join();
#
class myProcess(multiprocessing.Process):
    def run(self):
        n=5
        while n>0:
            print(n)
            time.sleep(1)
            n-=1
if __name__ == '__main__':
    p=myProcess()
    p.start()
    p.join()
