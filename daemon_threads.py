# daemon threads: a thread that runs in the background, not important for program to run
# your program will not wait for daemon threads to complete before existing
# non-daemon threads cannot normally be killed, stay alive until task is complete
# ex: background task, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: {} seconds".format(count))


x = threading.Thread(target=timer, daemon=True)
x.setDaemon(True)
x.start()


print(x.isDaemon())
answer = input('Do you wish to exit?')