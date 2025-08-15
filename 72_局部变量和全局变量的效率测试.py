import time
import math
def test01():
    start=time.time()
    for i in range(10000000):
        math.sqrt(30)
    end=time.time()
    print(end-start)

def test02():
    b=math.sqrt
    start=time.time()
    for i in range(10000000):
        b(30)
    end=time.time()
    print(end-start)

test01()
test02()