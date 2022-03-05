import threading
import random
import time
from functools import reduce
start=time.time()
def func(number):    
    random_list = random.sample(range(10), number)
    print(reduce(lambda x, y: x*y, random_list))
    
    
number = 5
thread1 = threading.Thread(target=func, args=(number,))
thread2 = threading.Thread(target=func, args=(number,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end=time.time()
print("execution time is:",round(end-start,2),"seconds")
