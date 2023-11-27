import struct
import time
import socket

ICMP_ECHO_REQUEST = 8  # Platform specific
DEFAULT_TIMEOUT = 2  # 超时时间
DEFAULT_COUNT = 4  # 默认发送次数

class IcmpPingSend():
    def checksum_calculation(self,ThreadID):
        my_checksum = 0
        header_false = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ThreadID, 1)
        #类型，代码，校验和，标识符，序号。
        #为什么发送8.0，因为这是个请求包，差错控制。参考https://blog.csdn.net/qq_40276626/article/details/120371213
        bytes_In_double = struct.calcsize("d")  # 给定字节数，d=8
        data = (192 - bytes_In_double) * "Q"  # 填充184个q，这里就是把前面的时间占位减去。
        data = struct.pack("d", time.time()) + bytes(data.encode('utf-8'))
        #计算真的校验和
        my_checksum = IcmpPingSend.do_checksum(header_false + data)  # 校验和，把icmp头和内容拼接起来，注意header和data加起来正好256
        header = struct.pack(
            "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ThreadID, 1
        )
        return header,data
    def do_checksum(source_string):  # 5运行,计算校验和
        sum = 0
        max_count = (len(source_string) / 2) * 2
        count = 0
        while count < max_count:
            sum+= source_string[count] + (source_string[count + 1] << 8)
            count = count + 2#两个为一组
        if max_count < len(source_string):  # 如果是奇数，就把最后一个数拼接上
            sum += ord(source_string[-1])
        sum = (sum >> 16) + (sum & 0xffff)#十六进制
        sum = sum + (sum >> 16)
        answer = ~sum & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)##移位指的是对应二进制移位，例如1<<2 1往左两位就是001就是100又8421得4
        return answer