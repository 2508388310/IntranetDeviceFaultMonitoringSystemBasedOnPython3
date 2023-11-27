# coding=utf-8

from time import sleep
import os
import sys
# sys.path.append(os.getcwd())
import pySQL

sys.path.append(r'E:\论文\项目20229.21\lunwen2\LANscanning')
import socket
# import PythonJson
import queue
import MultiThreadedModule
import DataStorageConversionModule as DSCM
def StartSearch():
  # PythonJson.PythonJson()
  find_ip_queue(Intranet_fixed_IP_segment())
def Intranet_fixed_IP_segment():#格式192.168.xx.
  hostname = socket.gethostname()
  ip = socket.gethostbyname(hostname)#本地ip
  print(ip)
  pySQL.creat_table()#打开数据库并创建数据表
  #pySQL.insert_new_data(locallhost=ip)
  fixed_IP_segment = '.'.join(ip.split('.')[:-1])
  return fixed_IP_segment
# def get_os():#获取本机信息
#   os = platform.system()
#   if os == "windows":
#     return "n"
#   else:
#     return "c"

def find_ip_queue(fixed_IP_segment):
  global time#一些必要的设置
  workqueue=queue.Queue(256)#队列上限
  threads=[]#线程队列
  threadID=1
  for i in range(0,256):# 组合新的ip（目标ip）
    ip = ('%s.%s' % (fixed_IP_segment, i))
    workqueue.put(ip)
  exit_flag = 0#队列是否为空特征码，1为空，0为非空
  while not exit_flag == 1:
    if workqueue.empty():
      exit_flag=1
    else:
      ip = workqueue.get()
      thread = MultiThreadedModule.myThread(threadID, ip)#线程模块
      thread.start()
      threads.append(thread)  # 线程管道集合
      threadID += 1

  sleep(10)

  DSCM.PythonJsonConversion().ListTransferredToJson()



if __name__ == "__main__":
  # pySQL.creat_table()#打开数据库并创建数据表
  # PythonJson.PythonJson()
  # find_ip_queue(Intranet_fixed_IP_segment())
  StartSearch()