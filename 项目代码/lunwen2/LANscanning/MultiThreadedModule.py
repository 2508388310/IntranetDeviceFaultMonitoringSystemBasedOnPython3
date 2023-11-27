import threading
from LANscanning.IcmpDetectionModule import icmp_ping


class myThread(threading.Thread):
  def __init__(self, threadID,ip):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.ip=ip
  def run(self):
    ping_ip(ip_str=self.ip,name=self.name)#此处选择ping命令，icmp协议
def ping_ip(ip_str,name):
  pinger= icmp_ping.Pinger(target_host=ip_str)#只是一个传值
  pinger.ping(name)#开始运行