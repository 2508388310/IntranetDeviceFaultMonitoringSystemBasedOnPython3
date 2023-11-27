import msgpack

import http.client
from metasploit.msfrpc import MsfRpcClient
try:

    HOST = "192.168.31.171"

    PORT = "65533"

    #headers = {"Content-type": "binary/message-pack"}

    # 连接MSF RPC Socket

    req = http.client.HTTPConnection(HOST, PORT)

    options = ["auth.login", "msf", "msf"]

    # 对参数进行序列化(编码)

    options = msgpack.packb(options)

    # 发送请求，序列化之后的数据包

    req.request("POST", "/api/1.0", body=options, headers=headers)

    # 获取返回

    res = req.getresponse().read()

    # 对返回进行反序列户(解码)

    res = msgpack.unpackb(res)

    res = res[b'token'].decode()

    print(res)
except Exception as e:
    print(e)
