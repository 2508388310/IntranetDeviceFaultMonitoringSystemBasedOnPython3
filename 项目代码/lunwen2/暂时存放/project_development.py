import project_development_pySQL
import nmap
import re
def find_ip_port():
    nm = nmap.PortScanner(nmap_search_path=('nmap', r"D:\nmap\nmap.exe"))
    #nm.scan('192.168.31.179', '1-200')
    # for host in nm.all_hosts():
    #     print('Host:%s(%s)'%(host,nm[host].hostnarne ()))
    #     print('state:%s'%nm[host].state())
    #     print(nm.command_line())
    # for proto in nm[host].all_protocols():
    #     print('protocol:%s'%proto)
    #     lport=nm[host][proto].keys()
    #     lport.sort()
    nm.scan(hosts='127.0.0.1',arguments='-PS')  # 扫描整个网段得主机的20-100端口
      # 本次扫描的命令
    #print(nm.command_line())
    nm.all_hosts()  # 扫描的所有主机
    ceshi=nm.scaninfo()  # 扫描的信息列出一个结构
    #print(ceshi)
      # 返回值用csv输出
    global datacsv
    datacsv=nm.csv()
    #print(datacsv)
    try:
        p=re.search(r"host(.*)cpe",datacsv)#条件1
        table=p.group()
    except Exception as e:
        print(e)
    a=table.split(';')
    return a
def find_ip_port1():
    # try:
    #     #p=re.search(r'(\w|\d)(.*?)(\;)(\1)',datacsv)
    #     #p = re.search(r'\s(\d+|\w+)\s', datacsv)
    #     p = re.search(r'(\w+|\d+|\.|\;)+(\-)+(\w+|\d+|\.|\;)+', datacsv)
    #     table = p.group()#'NoneType' object has no attribute 'group'没元素
    #     print(table)
    #     print("1")
    # except Exception as e:
    #     print(e)
    global ceshi
    ceshi=datacsv.split('\r\n')
    return ceshi




    # for i in range(0,10):
    #     print(a[i])
    # try:#
    #     p=re.compile(r"host(.*)cpe")#条件1
    #     talk=p.finditer(a)
    #     for i in talk:
    #         weizhi=i
    #         print(weizhi)
    #
    # except Exception as e:
    #     print(e)
    ## p = re.compile(r'\ \d\d\)')
    # p = re.compile(r'(^match=(\S)+)')
    # iter = p.finditer(weizhi1)
    # print(iter)
    # for m in iter:
    #     print(m)
    # for key in dict_1:
    #     print(key, ":", dict_1[key])
    # print(nm.scaninfo())
    # for host in nm.all_hosts():
    #     print('== == == == == == == == =')
    #     print(host)  # ip地址
    #print('State: % s' % nm[host].state())  # 主机存活状态

if __name__ == "__main__":
    b=find_ip_port()
    ceshi=find_ip_port1()
    # for i in range(0,13):
    #     print(b[i])
    project_development_pySQL.db_connect(b)
    project_development_pySQL.insert_data(ceshi)

    # for ip in
    #     arg=""
    #     nm.scan(hosts=ip,arguments=arg)