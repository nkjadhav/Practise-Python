# pool eample
import time
from multiprocessing import Pool

def f(x):
    return x*x

t1 = time.time()
p = Pool(5)
x=map(f, range(10000))
t2 = time.time()

print(t2-t1)
