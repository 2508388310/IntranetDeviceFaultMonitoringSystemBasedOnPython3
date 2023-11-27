import sys
import time

import msgpack
import http.client
class Msfrpc:
    class MsfError(Exception):
        def __init__(self, msg):
            self.msg = msg
        def __str__(self):
            return repr(self.msg)
    class MsfAuthError(MsfError):
        def __init__(self, msg):
            self.msg = msg
    def __init__(self, opts=[]):
        self.host = opts.get('host') or "192.168.31.171"
        self.port = opts.get('port') or 55553
        self.uri = opts.get('uri') or "/api/"
        self.ssl = opts.get('ssl') or False
        self.authenticated = False
        self.token = False
        self.headers = {"Content-type": "binary/message-pack"}
        if self.ssl:
            self.client = http.client.HTTPSConnection(self.host, self.port)
        else:
            self.client = http.client.HTTPConnection(self.host, self.port)
    def encode(self, data):
        return msgpack.packb(data)

    def decode(self, data):

        return msgpack.unpackb(data)

    def call(self, meth, opts=[]):

        if meth != "auth.login":

            if not self.authenticated:
                raise self.MsfAuthError("MsfRPC: Not Authenticated")

        if meth != "auth.login":
            opts.insert(0, self.token)

        opts.insert(0, meth)

        params = self.encode(opts)

        self.client.request("POST", self.uri, params, self.headers)

        resp = self.client.getresponse()

        return self.decode(resp.read())

    def login(self, user, password):

        ret = self.call('auth.login', [user, password])

        if ret.get('result') == 'success':
            self.authenticated = True
            self.token = ret.get('token')
            return True
        else:
            try:
                raise self.MsfAuthError("MsfRPC: Authentication failed")
            except Exception as e:
                print(e)








if __name__ == '__main__':


    # Create a new instance of the Msfrpc client with the default options

    client = Msfrpc({})

    # Login to the msfmsg server using the password "abc123"

    client.login('msf','msf')

    try:

        res = client.call('console.create')

        console_id = res['id']

    except:

        print("Console create failed ")

        sys.exit()

    host_list = '192.168.31.171'
    cmd = """search windows xp
        """

    # # cmd = """use exploit/windows/smb/ms08_067_netapi
    # #
    # #     set RHOST 192.168.31.170
    # #
    # #     exploit
    #
    #     """

    client.call('console.write',[console_id,cmd])

    time.sleep(1)

    while True:

        res = client.call('console.read',[console_id])

        if len(res['data']) > 1:

                print(res['data'])

        if res['busy'] == True:

                time.sleep(1)

                continue

        break

    client.call('console.destroy',[console_id])