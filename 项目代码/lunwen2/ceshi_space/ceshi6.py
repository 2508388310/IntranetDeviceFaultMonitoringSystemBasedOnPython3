#!/usr/bin/python3.6.4
#-*-coding:utf-8-*-
__author__ = 'Rosefinch'
__date__ = '2018/5/31 10:32'


def chesksum(data):
	"""
	校验
	"""
	n = len(data)
	m = n % 2 #判断data长度是否是偶数字节
	sum = 0 #记录(十进制)相加的结果
	for i in range(0, n - m ,2): #将每两个字节(16位)相加（二进制求和）直到最后得出结果
		sum += ord(data[i]) + (ord(data[i+1]) << 8)
	#传入data以每两个字节（十六进制）通过ord转十进制，第一字节在低位，第二个字节在高位
	if m: #传入的data长度是奇数，将执行，且把这个字节（8位）加到前面的结果
		sum += ord(data[-1])
	#将高于16位与低16位相加
	sum = (sum >> 16) + (sum & 0xffff)
	sum += (sum >> 16) #如果还有高于16位，将继续与低16位相加
	answer = ~sum & 0xffff
	#对sum取反(返回的是十进制)
	#主机字节序转网络字节序列（参考小端序转大端序）
	answer = answer >> 8 | (answer << 8 & 0xff00)
	return answer #最终返回的结果就是wireshark里面看到的checksum校验和

if __name__ == "__main__":
	# data = "\x08\x00\x00\x01\x00\x01\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x61\x62\x63\x64\x65\x66\x67\x68\x69"
	data_type = '\x08' # ICMP Echo Request
	data_code = '\x00' # must be zero
	data_checksum = '\x00\x00' # "...用值0替换该字段..."
	data_ID = '\x00\x01' #标识符
	data_Sequece = '\x00\x01' #序列号
	payload_body = 'abcdefghijklmnopqrstuvwabcdefghi' #data
	icmp_message = data_type + data_code + data_checksum + data_ID + data_Sequece + payload_body

	int_ = chesksum(icmp_message)
	print('{:d} --->  {:x}'.format(int_,int_))
