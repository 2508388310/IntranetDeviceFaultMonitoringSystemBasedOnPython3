import struct
import time

import select

from LANscanning.DataStorageConversionModule import PythonJsonConversion
from LANscanning.IcmpDetectionModule import icmp_result


class IcmpPingPong():
    def receive_pong(self,sock, ID, timeout, target_addr, name):  # 6接收返回（监听）,可运行（pong的意思就是监听）
        time_remaining = timeout
        while True:
            start_time = time.time()  # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
            readable = select.select([sock], [], [], time_remaining)
            # 参考https://blog.csdn.net/samsam2013/article/details/78554073
            time_spent = (time.time() - start_time)  # select的时间
            if readable[0] == []:  # Timeout
                IcmpResult=icmp_result.start(19, 0, target_addr)
                PythonJsonConversion.StagingList(self,target_addr=target_addr,IcmpResult=IcmpResult,name=name,symbol=0)
                return
            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]  # 直接字节流截取输出，这里有极大的问题可能是网络层的，也可能是节取得有问题
            type, code, checksum, packet_ID, sequence = struct.unpack(
                "bbHHh", icmp_header
            )  # 有问题

            if packet_ID == ID:#判断是不是对应程序线程接收
                bytes_In_double = struct.calcsize("d")  # calsize 计算按照格式 fmt 打包的结果有多少个字节。8
                time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
                IcmpResult=icmp_result.start(type, code, target_addr)  # 进入数据库
                PythonJsonConversion.StagingList(self,target_addr=target_addr, IcmpResult=IcmpResult, name=name, symbol=1)

                return time_received - time_sent  # 判断发送了多长时间，成功的，
                # 现在的时间-发包时间

                # 数据包的超时时间判断，time_remaining是超时时间
            time_remaining = time_remaining - time_spent  # 超时时间-等待时间
            # 可能发送数据包（里面是0,0），发出去后两条路①超时没法出去②发出去了但是目标不可达就是里面是别的数
            if time_remaining <= 0:
                # 两个超时，一个是根本没发出去。一个是发出去啥都对了超时了
                IcmpResult=icmp_result.start(19, 0, target_addr, name)  # 进入数据库
                PythonJsonConversion.StagingList(target_addr, IcmpResult, name, symbol=0)
                return  # 超时才会返回