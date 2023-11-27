#!/usr/bin/env python
# coding=utf-8
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 3.5.2.
# Instructions to make it run with Python 2.7.x is given below.
# It may run on any other version with/without modifications.
import os
import socket
# import struct
# import select
# import time
# import icmp_result
import IcmpPingPong as IPP
import IcmpPingSend as IPS
ICMP_ECHO_REQUEST = 8  # Platform specific
DEFAULT_TIMEOUT = 2  # 超时时间
DEFAULT_COUNT = 4  # 默认发送次数
class Pinger(object):
    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):  # 1运行
        #print("6")

        self.target_host = target_host  # 组合的ip
        self.count = count
        self.timeout = timeout
    # def do_checksum(self, source_string):  # 5运行,计算校验和
    #     sum = 0
    #     max_count = (len(source_string) / 2) * 2
    #     count = 0
    #     while count < max_count:
    #         sum+= source_string[count] + (source_string[count + 1] << 8)
    #         count = count + 2#两个为一组
    #     if max_count < len(source_string):  # 如果是奇数，就把最后一个数拼接上
    #         sum += ord(source_string[-1])
    #     sum = (sum >> 16) + (sum & 0xffff)
    #     sum = sum + (sum >> 16)
    #     answer = ~sum & 0xffff
    #     answer = answer >> 8 | (answer << 8 & 0xff00)##移位指的是对应二进制移位，例如1<<2 1往左两位就是001就是100又8421得4
    #     return answer

    # def receive_pong(self, sock, ID, timeout,target_addr,name):  # 6接收返回（监听）,可运行（pong的意思就是监听）
    #     time_remaining = timeout
    #     while True:
    #         start_time = time.time()#返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    #         readable = select.select([sock], [], [], time_remaining)
    #         #参考https://blog.csdn.net/samsam2013/article/details/78554073
    #         time_spent = (time.time() - start_time)#select的时间
    #         if readable[0] == []:  # Timeout
    #             icmp_result.start(19, 0, target_addr, name)
    #             return
    #         time_received = time.time()
    #         recv_packet, addr = sock.recvfrom(1024)
    #         icmp_header = recv_packet[20:28]#直接字节流截取输出，这里有极大的问题可能是网络层的，也可能是节取得有问题
    #         type, code, checksum, packet_ID, sequence = struct.unpack(
    #             "bbHHh", icmp_header
    #         )#有问题
    #
    #         if packet_ID == ID:
    #
    #             bytes_In_double = struct.calcsize("d")#calsize 计算按照格式 fmt 打包的结果有多少个字节。8
    #             time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
    #             icmp_result.start(type, code, target_addr, name)  # 进入数据库
    #
    #             return time_received - time_sent  # 判断发送了多长时间，成功的，
    #             # 现在的时间-发包时间
    #
    #             # 数据包的超时时间判断，time_remaining是超时时间
    #         time_remaining = time_remaining - time_spent#超时时间-等待时间
    #         # 可能发送数据包（里面是0,0），发出去后两条路①超时没法出去②发出去了但是目标不可达就是里面是别的数
    #         if time_remaining <= 0:
    #             #两个超时，一个是根本没发出去。一个是发出去啥都对了超时了
    #
    #             icmp_result.start(19, 0, target_addr, name)  # 进入数据库
    #             return  # 超时才会返回
    #             #-------------------------------------------------------------------
    #             #发送的假数据包，py程序发出去了，到达路由器。发出去就是有信息回来，没法出去就是超时了。
    #             # time_remaining = time_remaining - time_spent
    #             # if time_remaining <= 0:
    #             #     print('超时超时超时超时超时超时超时超时超时超时超时超时')
    #             #     icmp_result.start(19, 0, target_addr, name)  # 进入数据库
    #             #     # 这里判断的是，有时间负数的情况。返回为none
    #             #     return  # 超时才会返回
    #             # else:
    #             #     return time_received - time_sent#判断发送了多长时间，成功的

            #可能发送数据包（里面是0,0），发出去后两条路①超时没法出去②发出去了但是目标不可达就是里面是别的数

    # def checksum_calculation(self,ThreadID):
    #     my_checksum = 0
    #     header_false = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ThreadID, 1)
    #     #类型，代码，校验和，标识符，序号。
    #     #为什么发送8.0，差错控制。参考https://blog.csdn.net/qq_40276626/article/details/120371213
    #     bytes_In_double = struct.calcsize("d")  # 给定字节数，d=8
    #     data = (192 - bytes_In_double) * "Q"  # 填充184个q，这里就是把前面的时间占位减去。
    #     data = struct.pack("d", time.time()) + bytes(data.encode('utf-8'))
    #     my_checksum = self.do_checksum(header_false + data)  # 校验和，把icmp头和内容拼接起来，注意header和data加起来正好256
    #     header = struct.pack(
    #         "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ThreadID, 1
    #     )
    #     return header,data
    def send_ping(self,ThreadID,sock):  # 4运行，只是发送
        # header,data= self.checksum_calculation(ThreadID)
        # packet = header + data
        # #该他了
        # sock.sendto(packet, (self.target_host, 1))
        header,data=IPS.IcmpPingSend.checksum_calculation(self,ThreadID)#校验和计算
        packet = header + data
        sock.sendto(packet, (self.target_host, 1))




    def ping_once(self,name):  # 3运行，用来检查，向目标主机发送一次查验
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        except socket.error as e:
            if e.errno == 1:
                e.msg += "ICMP消息只能从管理员用户进程发送"
                raise socket.error(e.msg)
        except Exception as e:
            print("Exception: %s" % (e))
        ThreadID = os.getpid() & 0xFFFF#线程id作为返回包区别线程的特征

        #发送
        self.send_ping(ThreadID,sock)#发送到目标主机（发送和计算校验和）
        #接收
        #self, sock, ID, timeout, target_addr,
        delay = IPP.IcmpPingPong.receive_pong(self,sock=sock, ID=ThreadID, timeout=self.timeout, target_addr=self.target_host, name=name)

        sock.close()
        return delay
    def ping(self,name):  # 2运行，最后这俩属于验错误
        for i in range(self.count):#ping几次
            try:
                delay = self.ping_once(name=name)
            except socket.gaierror as e:
                # print("Ping 失败. (socket的错误: '%s')" % e[1])
                break
            if delay == None:#这个是超时
                pass
                # print("Ping 失败."+name+" (超时多长时间 %ssec.)" % self.timeout)
            else:
                pass
                # delay = delay * 1000#if线程=id的那个
                # print("在这个时间内成功返回"+name+" %0.4fms" % delay)

