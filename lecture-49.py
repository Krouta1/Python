# multi threading

#thred = a small unit of a process
#multi threading = multiple threads in a single process

#cpu bound = cpu bound tasks are those that are limited by the speed of the cpu, use multiprocessing

#io bound = io bound tasks are those that are limited by the speed of the input/output devices, use multithreading

import threading
import time

#print(threading.active_count()) #number of active threads

#print(threading.enumerate()) #list of active threads

#program to run a function in a thread


def eat_breakfast(): # io bound task
    time.sleep(3)
    print('You ate breakfast')

def drink_coffee(): # io bound task
    time.sleep(4)
    print('You drank coffee')

def study(): # io bound task
    time.sleep(5)
    print('You studied')

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()
#with multithreading, the tasks are executed concurrently, so the total time taken is 5 seconds, not 12 seconds

x.join()
y.join()
z.join()
