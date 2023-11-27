#!/usr/bin/env python
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
        self.port = opts.get('port') or 65533
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
            raise self.MsfAuthError("MsfRPC: Authentication failed")
        # if ret.get('result') == 'success':
        #     raise self.MsfAuthError("MsfRPC: Authentication failed")
        # else:
        #     self.authenticated = True
        #     self.token = ret.get('token')
        #     return True

if __name__ == '__main__':

    # Create a new instance of the Msfrpc client with the default options
    client = Msfrpc({})

    # Login to the msfmsg server using the password "abc123"
    client.login('msf', 'msf')

    # Get a list of the exploits from the server
    mod = client.call('module.exploits')

    # Grab the first item from the modules value of the returned dict
    print("Compatible payloads for : %s\n" % mod['modules'][0])


    # Get the list of compatible payloads for the first option
    ret = client.call('module.compatible_payloads', [mod['modules'][0]])
    for i in (ret.get('payloads')):
        print("\t%s" % i)

