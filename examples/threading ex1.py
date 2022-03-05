import threading
def calc_square(number):
    print('Square:',number*number)
def calc_quad(number):
    print('Quad:',number*number*number*number)

number = 7
thread1=threading.Thread(target=calc_square,args=(number,))
thread2=threading.Thread(target=calc_quad, args=(number,))

thread1.start()
thread1.join()
thread2.start()
thread2.join()
