# loops = [4, 2,8]
# print(len(loops))
# import queue
# exit_flag=0
# workqueue=queue.Queue(10)
# for i in range(10):
#     workqueue.put(i)
# while not exit_flag==1:
#     if workqueue.empty():
#       exit_flag=1
#     else:
# import os
# a=-1
# print(os.getpid())
# print(os.getppid())
# my_ID = a & 0xFFFF
# print(my_ID)
# b=my_ID % 0xFFFF
# print(b)

import socket
# icmp = socket.getprotobyname("tcp")
# print(icmp)
a='192.168.101.4'
target_addr = socket.gethostbyname(a)
print(target_addr)