from multiprocessing import Process, Queue


# 写数据进程执行的代码：
def write(q):
    for value in ['A', 'B', 'C']:
        print("Put  %s  to queue...", value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get  %s  from queue.", value)
            time.sleep(random.random())
        else:
            break
# coding:utf-8
from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s   开始执行，进程号为%d", (msg, os.getpid()))
    #  random.random()随机生成0-1之间的浮点数
    time.sleep(random.random(), 2)
    t_stop = time.time()
    print(msg, '执行完毕，耗时%0.2f%', (t_stop - t_start))

# import  threading
# import  time,mutex
# class MyThread(threading.Thread):
#     def  run(self):
#         global  num
#         time.sleep(1)
#
#         if  mutex.acquire(1):
#             num +=1
#             msg  =  self.name  +  'set  num  to  '   +str(num)
#         print  msg
#         mutex.release()
#         num  =  0
#         mutex  =  threading.Lock()
#     def  test():
#         for   i  in  range(5):
#             t  =   MyThread()
#             t.start()
#
#     test()


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw  ，写入：
    pw.start()
    # 等待pw结束
    pw.join()
    # 启动子进程pr，读取：
    pr.start()
    pr.join()
    # pr   进程里是死循环，无法等待其结束，只能强行终止:
    print('')
    print('所有数据都写入并且读完')

    po = Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(0, 10):
        po.apply_async(worker, (i,))
    print("---start --- ")
    po.close()
    po.join()
    print("----end --- ")

