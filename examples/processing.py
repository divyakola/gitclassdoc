import multiprocessing
import random
from functools import reduce
def func(number):
    random_list = random.sample(range(10), number)
    print(reduce(lambda x, y: x*y, random_list))    
number = 5
process1 = multiprocessing.Process(target=func, args=(number,))
process2 = multiprocessing.Process(target=func, args=(number,))
if __name__=='__main__':
    process1.start()
    process2.start()
    process1.join()
    process2.join()
