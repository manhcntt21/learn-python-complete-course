# thread: a flow of execution. Like a separate order of instruction
# however, each thread takes a turn running to achieve concurrency
# GIL (global interpreter lock)
# allows only one thread to hold the control of the Python interpreter


# cpu bound: program/task spends most of it's time waiting for internal events (cpu intensive) use multiprocessing

# io bound: program/task spends most of it's time waiting for external events (user input, web scraping)
# use multithreading

import threading
import time


# three tasks in the morning
def eat_breakfast():
    time.sleep(3)
    # for i in range(5):
    #     print('eat_breakfast {}'.format(i))
    print('you have breakfast')


def drink_coffee():
    time.sleep(4)
    # for i in range(5):
    #     print('drink_coffee {}'.format(i))
    print('you drink a cup of coffee')


def study():
    time.sleep(5)
    # for i in range(5):
    #     print('study {}'.format(i))
    print('you study at school')


# sequentially
# eat_breakfast()
# drink_coffee()
# study()
# 12 secs
# print(threading.active_count())  # 1
# print(threading.enumerate())

# concurrency
x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

# x.join() # thread main must wait each thread finished
# y.join()
# z.join()

print(threading.active_count())  # 4
print(threading.enumerate())
print(time.perf_counter())  # time for main thread

