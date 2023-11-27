import pySQL
def start(type,code,target_addr):
    print("123123123")
    if type==0:
        if code==0:
            result='%s---回显应答'%target_addr
            print('%s---回显应答'%target_addr)


            print("123456")
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, symbol=1)
            print("1")
            return '%s---回显应答' % target_addr
    elif type==3:
        if code==0:
            print('%s---网络不可达' % target_addr)
            result='%s---网络不可达' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result)
            print("1")
            return '%s---网络不可达' % target_addr
        elif code==1:
            return '%s---主机不可达' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
            print("1")
        elif code==2:
            return '%s---协议不可达 ' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
            print("1")
        elif code==3:
            return '%s---端口不可达 ' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
            print("1")
        elif code==4:
            return '%s---需要进行分片但设置不分片比特' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==5:
            return '%s---源站选路失败' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==6:
            return '%s---目的网络未知' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==7:
            return '%s---目的主机未知' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==8:
            return '%s---源主机被隔离（作废不用）' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==9:
            return '%s---目的网络被强制禁止' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==10:
            return '%s---目的主机被强制禁止' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==11:
            return '%s---由于服务类型TOS，网络不可达' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==12:
            return '%s---由于服务类型TOS，主机不可达' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==13:
            return '%s---由于过滤，通信被强制禁止' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==14:
            return '%s---主机越权' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==15:
            return '%s---优先中止生效' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 4:
        if code==0:
            return '%s---对网络重定向' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
            print("1")
    elif type == 5:
        if code==0:
            return '%s---对网络重定向' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
            #print("1")
        elif code==1:
            return '%s---优先中止生效' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==2:
            return '%s---对服务类型和网络重定向' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code==3:
            return '%s---对服务类型和主机重定向' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 8:
        if code == 0:
            return '%s---回显请求（Ping请求）' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 9:
        if code == 0:
            return '%s---路由器通告' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 10:
        if code == 0:
            return '%s---路由器请求' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 11:
        if code == 0:
            return '%s---路由器通告' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
            #在数据报组装期间生存时间为0
        elif code == 1:
            return '%s---在数据报组装期间生存时间为0' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 12:
        if code == 0:
            return '%s---坏的IP首部（包括各种差错）' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
        elif code == 1:
            return  '%s---缺少必需的选项' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 13:
        if code == 0:
            return '%s---时间戳请求（作废不用）' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 14:
        if code == 0:
            return '%s---路由器通告' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 15:
        if code == 0:
            return '%s---信息请求（作废不用）' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 16:
        if code == 0:
            return  '%s---信息应答（作废不用）' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 17:
        if code == 0:
            return '%s---地址掩码请求' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 18:
        if code == 0:
            return '%s---地址掩码应答' % target_addr
            #pySQL.insert_new_data(target_ip=target_addr, icmp_result=result, name=name)
    elif type == 19:
        if code == 0:
            print('%s---超时' % target_addr)
            result='%s---超时' % target_addr
            pySQL.insert_new_data(target_ip=target_addr, icmp_result=result)
            return '%s---超时' % target_addr





