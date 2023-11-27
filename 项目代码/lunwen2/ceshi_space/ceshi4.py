# #! /usr/bin/python
# # -*-coding:UTF-8-*-
#
# import threading
# from time import sleep
# from datetime import datetime
#
# loops = [4, 2]#列表4和2
# date_time_format = '%y-%M-%d %H:%M:%S'
#
# def date_time_str(date_time):
#     return datetime.strftime(date_time, date_time_format)
#
# def loop(n_loop, n_sec):
#     print('线程（', n_loop, '）开始执行:',
#            date_time_str(datetime.now()), '，先休眠（', n_sec, '）秒')
#     sleep(n_sec)
#     print('线程（', n_loop, '）休眠结束，结束于:', date_time_str(datetime.now()))
#
# def main():
#     print('---所有线程开始执行:', date_time_str(datetime.now()))
#     threads = []#线程空间
#     n_loops = range(len(loops))#返回2，就是返回list中的个数。注意range走后的取不到2就是0,1
#
#     for i in n_loops:
#          t = threading.Thread(target=loop, args=(i, loops[i]))
#          threads.append(t)#先把线程准备好再开始
#
#     for i in n_loops:    # start threads
#          threads[i].start()
#
#     for i in n_loops:    # wait for all
#          threads[i].join() # threads to finish
#
#     print('---所有线程执行结束于:', date_time_str(datetime.now()))
#
# if __name__ == '__main__':
#     main()

#! /usr/bin/python
# -*-coding:UTF-8-*-

# import threading
# from time import sleep
# from datetime import datetime
#
# loops = [4, 2]
# date_time_format = '%y-%M-%d %H:%M:%S'
#
# class ThreadFunc(object):
#     def __init__(self, func, args, name=''):
#          self.name = name
#          self.func = func
#          self.args = args
#
#     def __call__(self):#参考https://blog.csdn.net/fengbingchun/article/details/122330858
#         #就是ans = 类名()之后ans(10, 20)<=>ans.__call__(10, 20)
#          self.func(*self.args)
#
#     # *self._args
#     # 表示接受元组类参数；
#     # ** kwargs
#     # 表示接受字典类参数
#
# def date_time_str(date_time):
#     return datetime.strftime(date_time, date_time_format)
#
# def loop(n_loop, n_sec):
#     print('线程（', n_loop, '）开始执行:',
#            date_time_str(datetime.now()), '，先休眠（', n_sec, '）秒')
#     sleep(n_sec)
#     print('线程（', n_loop, '）休眠结束，结束于:', date_time_str(datetime.now()))
#
# def main():
#     print('---所有线程开始执行:', date_time_str(datetime.now()))
#     threads = []
#     nloops = range(len(loops))
#
#     for i in nloops: # create all threads
#          t = threading.Thread(
#              target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
#          threads.append(t)
#
#     for i in nloops: # start all threads
#          threads[i].start()
#
#     for i in nloops: # wait for completion
#          threads[i].join()
#
#     print('---所有线程执行结束于:', date_time_str(datetime.now()))
#
# if __name__ == '__main__':
#     main()
#! /usr/bin/python
# -*-coding:UTF-8-*-


#! /usr/bin/python
# -*-coding:UTF-8-*-

# import threading
# from time import sleep
# from datetime import datetime
#
# loops = [4, 2]
# date_time_format = '%y-%M-%d %H:%M:%S'
#
# def date_time_str(date_time):
#     return datetime.strftime(date_time, date_time_format)
#
# def loop(n_loop, n_sec):
#     print('线程（', n_loop, '）开始执行:',
#            date_time_str(datetime.now()), '，先休眠（', n_sec, '）秒')
#     sleep(n_sec)
#     print('线程（', n_loop, '）休眠结束，结束于:', date_time_str(datetime.now()))
#
# def main():
#     print('---所有线程开始执行:', date_time_str(datetime.now()))
#     threads = []
#     n_loops = range(len(loops))
#
#
#         thread1 = MyThread(1, "Thread-1", 1)
#         thread2 = MyThread(2, "Thread-2", 2)
#
#         # 开启新线程
#         thread1.start()
#         thread2.start()
#
#         # 添加线程到线程列表
#         threads.append(thread1)
#         threads.append(thread2)
#
#         # 等待所有线程完成
#         for t in threads:
#              t.join()
#         print("退出主线程")
#
#     print('---所有线程执行结束于:', date_time_str(datetime.now()))
#
# if __name__ == '__main__':
#     main()



import threading
from time import sleep
from datetime import datetime

loops = [4, 2,4, 2,4]
date_time_format = '%y-%M-%d %H:%M:%S'

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
         threading.Thread.__init__(self)
         self.name = name
         self.func = func
         self.args = args

    def getResult(self):
         return self.res

    def run(self):#特殊函数，参考：https://blog.csdn.net/qq_37718585/article/details/123384784
        #用以表示线程活动的方法
         print('starting', self.name, 'at:', date_time_str(datetime.now()))
         self.res = self.func(*self.args)
         print(self.name, 'finished at:', date_time_str(datetime.now()))

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec):
    print('线程（', n_loop, '）开始执行:',
           date_time_str(datetime.now()), '，先休眠（', n_sec, '）秒')
    sleep(n_sec)
    print('线程（', n_loop, '）休眠结束，结束于:', date_time_str(datetime.now()))

def main():
    print('---所有线程开始执行:', date_time_str(datetime.now()))
    threads = []
    # n_loops = range(len(loops))

    # n_loops = range(loops)

    for i in range(0, 5):
         t = MyThread(loop, (i, loops[i]),
         loop.__name__)
         threads.append(t)

    for i in range(0, 5):
         threads[i].start()

    for i in range(0, 5):
         threads[i].join()

    print('---所有线程执行结束于:', date_time_str(datetime.now()))
if __name__ == '__main__':
    main()


#! /usr/bin/python
# -*-coding:UTF-8-*-
#
# import threading
# from time import sleep
# from datetime import datetime
#
# date_time_format = '%y-%M-%d %H:%M:%S'
#
# class MyThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#          threading.Thread.__init__(self)
#          self.threadID = threadID
#          self.name = name
#          self.counter = counter
#
#     def run(self):
#          print ("开启线程： " + self.name)
#          # 获取锁，用于线程同步
#          threadLock.acquire()
#          print_time(self.name, self.counter, 3)
#          # 释放锁，开启下一个线程
#          threadLock.release()
#
# def date_time_str(date_time):
#     return datetime.strftime(date_time, date_time_format)
#
# def print_time(threadName, delay, counter):
#     while counter:
#          sleep(delay)
#          print ("%s: %s" % (threadName, date_time_str(datetime.now())))
#          counter -= 1
#
# def main():
#     # 创建新线程
#     thread1 = MyThread(1, "Thread-1", 1)
#     thread2 = MyThread(2, "Thread-2", 2)
#
#     # 开启新线程
#     thread1.start()
#     thread2.start()
#
#     # 添加线程到线程列表
#     threads.append(thread1)
#     threads.append(thread2)
#
#     # 等待所有线程完成
#     for t in threads:
#          t.join()
#     print("退出主线程")
#
# if __name__ == "__main__":
#     threadLock = threading.Lock()
#     threads = []
#     main()

