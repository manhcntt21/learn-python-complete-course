# multi-processing
# running tasks in parallel on different cpu cores, bypasses GIL used for thread
# multi-processing: better for cpu bound tasks (heavy cpu uasge)
# multi-threading: better for io bound tasks (waiting around)


from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())
    a1 = Process(target=counter, args=(125000000, ))
    a2 = Process(target=counter, args=(125000000, ))
    a3 = Process(target=counter, args=(125000000, ))
    a4 = Process(target=counter, args=(125000000, ))
    a5 = Process(target=counter, args=(125000000, ))
    a6 = Process(target=counter, args=(125000000, ))
    a7 = Process(target=counter, args=(125000000, ))
    a8 = Process(target=counter, args=(125000000, ))


    a1.start()
    a2.start()
    a3.start()
    a4.start()
    a5.start()
    a6.start()
    a7.start()
    a8.start()


    a1.join()
    a2.join()
    a3.join()
    a4.join()
    a5.join()
    a6.join()
    a7.join()
    a8.join()



    print('finish in: {} seconds'.format(time.perf_counter()))


if __name__ == '__main__':
    main()
