# import socket, select
#
# s = socket.socket()
# print('s:', s)
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
#
# s.listen(5)
#
# inputs = [s]
# while True:
#     rs, ws, es = select.select(inputs, [],
#                                [])  # 1、select函数阻塞进程，直到inputs中的套接字被触发（在此例中，套接字接收到客户端发来的握手信号，从而变得可读，满足select函数的“可读”条件），rs返回被触发的套接字（服务器套接字）；
#     # 4、select再次阻塞进程，同时监听服务器套接字和获得的客户端套接字；
#
#     for r in rs:
#         if r is s:  # 2、如果是服务器套接字被触发（监听到有客户端连接服务器）
#             c, addr = s.accept()
#             print('Got connection from', addr)
#             inputs.append(c)  # 3、inputs加入客户端套接字
#         else:  # 5、当客户端发送数据时，客户端套接字被触发，rs返回客户端套接字，然后进行下一步处理。
#             try:
#                 data = r.recv(1024)
#                 disconnected = not data
#             except socket.error:
#                 disconnected = True
#             if disconnected:
#                 print(r.getpeername(), 'disconnected')
#                 inputs.remove(r)
#             else:
#                 print(data)

#-----------------------------------------

# loops = [4, 2]
# print(len(loops))
# print(loops[0])
# print(range(len(loops)))



#-----------------------------------------


# -*- coding: utf-8 -*-
import os
import argparse
import socket
import struct
import select
import threading
import time
# 请求回显头
from concurrent.futures.thread import ThreadPoolExecutor
from tkinter import *
from tkinter import ttk

ICMP_ECHO_REQUEST = 8  # Platform specific
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 1
# 创建锁
lock = threading.Lock()
Running = True


class Pinger(object):
    """ Pings to a host -- the Pythonic way"""

    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
        self.target_host = target_host
        self.count = count
        self.timeout = timeout

    # 计算校验和
    def do_checksum(self, source_string):
        """  Verify the packet integritity """
        sum = 0
        max_count = (len(source_string) / 2) * 2
        count = 0
        while count < max_count:
            val = source_string[count + 1] * 256 + source_string[count]
            sum = sum + val
            sum = sum & 0xffffffff
            count = count + 2

        if max_count < len(source_string):
            sum = sum + ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff

        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

    def receive_pong(self, sock, ID, timeout):
        """
        Receive ping from the socket.
        """
        print('接收')
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []:  # Timeout
                return

            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type, code, checksum, packet_ID, sequence = struct.unpack(
                "bbHHh", icmp_header
            )
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack("d", recv_packet[28:28 + bytes_In_double])[0]
                return time_received - time_sent

            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return

    def send_ping(self, sock, ID):
        """
        Send ping to the target host
        """
        target_addr = socket.gethostbyname(self.target_host)

        my_checksum = 0

        # Create a dummy heder with a 0 checksum.
        header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "R"
        data = struct.pack("d", time.time()) + bytes(data.encode('utf-8'))

        # Get the checksum on the data and the dummy header.
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
            "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
        )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))
        print('发送')

    def ping_once(self):
        """
        Returns the delay (in seconds) or none on timeout.
        """
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error as e:
            if e.errno == 1:
                # Not superuser, so operation not permitted
                e.msg += "ICMP messages can only be sent from root user processes"
                raise socket.error(e.msg)
        except Exception as e:
            print("Exception: %s" % (e))

        my_ID = os.getpid() & 0xFFFF

        self.send_ping(sock, my_ID)
        delay = self.receive_pong(sock, my_ID, self.timeout)
        sock.close()
        return delay

    def ping(self):
        """
        Run the ping process
        """
        for i in range(self.count):
            # print("Ping to %s..." % self.target_host, )
            try:
                delay = self.ping_once()
            except socket.gaierror as e:
                return -2
                print("Ping failed. (socket error: '%s')" % e[1])
                break

            if delay == None:
                # return self.timeout
                return -2
                print("Ping failed. (timeout within %ssec.)" % self.timeout)
            else:
                delay = delay * 1000
                return delay
                print("Get ping in %0.4fms" % delay)


def closePool():
    global Running
    Running = False
    print("hah")


def clearTb():
    x = tb.get_children()
    for item in x:
        tb.delete(item)
    numlb['text'] = 0


def insertRes():
    global Running
    Running = True
    clearTb()
    timeout = int(t6.get()) / 1000
    threadnum = int(t7.get())
    print(threadnum)
    print(timeout)
    start = int(t4.get())
    end = int(t5.get())
    # run("www.baidu.com")
    pool = ThreadPoolExecutor(threadnum)
    for i in range(start, end):
        ip = t1.get() + '.' + t2.get() + '.' + t3.get() + '.' + str(i)
        v = pool.submit(run, ip, i, timeout)


def run(ipstart, i, timeout):
    global Running
    if (Running == False):
        return
    ping = Pinger(ipstart, timeout=timeout)
    res1 = ping.ping()
    res2 = ping.ping()
    res3 = ping.ping()
    if (res1 == -2 or res2 == -2 or res3 == -2):
        tb.insert("", i, value=(ipstart, "超时或错误"))
    else:
        res = (res1 + res2 + res3) / 3
        res = str(round(res, 4)) + 'ms'
        tb.insert("", i, value=(ipstart, res))



        lock.acquire()
        num = int(numlb['text'])
        num += 1
        numlb['text'] = num
        lock.release()


if __name__ == '__main__':
    # 创建  窗口
    root = Tk()
    # 先初始化

    root.title("一个简单的Python Ping程序         by Duskry Ren ")
    root.geometry("720x500")
    root.resizable(False, False)
    frame1 = Frame(root)
    frame1.pack()
    # frame1.place(x=0,y=0,width=720,height=50)
    lb1 = Label(frame1, text='   IP地址：', font=20)
    lb1.pack(side=LEFT)
    t1 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t1.pack(side=LEFT)
    t1.insert(0, '10')
    lb2 = Label(frame1, text='.', font=20)
    lb2.pack(side=LEFT)
    t2 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t2.pack(side=LEFT)
    t2.insert(0, "1")
    lb3 = Label(frame1, text='.', font=20)
    lb3.pack(side=LEFT)
    t3 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t3.pack(side=LEFT)
    t3.insert(0, "11")
    lb3 = Label(frame1, text='从', font=20)
    lb3.pack(side=LEFT)
    t4 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t4.pack(side=LEFT)
    t4.insert(0, "0")
    lb3 = Label(frame1, text='到', font=20)
    lb3.pack(side=LEFT)
    t5 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t5.pack(side=LEFT)
    t5.insert(0, "10")
    lb3 = Label(frame1, text=' 超时：', font=20)
    lb3.pack(side=LEFT)
    t6 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t6.pack(side=LEFT)
    t6.insert(0, "2000")
    lb3 = Label(frame1, text=' 线程：', font=20)
    lb3.pack(side=LEFT)
    t7 = Entry(frame1, font=20, textvariable=IntVar, width=6)
    t7.pack(side=LEFT)
    t7.insert(0, 3)
    frame2 = Frame(root, width=720, height=200)
    frame2.pack()
    scroll1 = Scrollbar(frame2)
    scroll1.pack(side=RIGHT, fill=Y)
    tb = ttk.Treeview(frame2, yscrollcommand=scroll1.set, show="headings", height=12)
    tb['columns'] = ("ip", "time")
    tb.column("ip", width=320, anchor='center')
    tb.column("time", width=320, anchor='center')
    tb.heading("ip", text='ip')
    tb.heading('time', text='状态')
    tb.pack()
    frame3 = Frame(root, bg='gray')
    frame3.pack(fill=X)
    btn1 = ttk.Button(frame3, text="开始", command=insertRes)
    btn1.pack(side=LEFT)
    btn2 = ttk.Button(frame3, text='结束', command=closePool)
    btn2.pack(side=LEFT)
    btn3 = ttk.Button(frame3, text="清空", command=clearTb)
    btn3.pack(side=LEFT)
    numlb = Label(frame3, text='0')
    numlb.pack(side=RIGHT)
    lb = Label(frame3, text="响应数：")
    lb.pack(side=RIGHT)
    # text = Text(frame2,font=26,yscrollcommand=scroll1.set)
    # text.pack(fill=BOTH, expand=YES)

    # insertRes()

    root.mainloop()
    # parser = argparse.ArgumentParser(description='Python ping')
    # parser.add_argument('host', action="store", help=u'主机名')
    # given_args = parser.parse_args()
    # target_host = given_args.host
    # pinger = Pinger(target_host='www.baidu.com')
    # pinger.ping()



