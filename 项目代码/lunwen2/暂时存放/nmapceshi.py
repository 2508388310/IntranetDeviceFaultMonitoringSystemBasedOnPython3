import nmap
nm = nmap.PortScanner(nmap_search_path=('nmap', r"D:\nmap\nmap.exe"))
nm.scan(hosts='192.168.31.179',arguments='-O')
nm.all_hosts()
datacsv=nm.csv()
print(datacsv)