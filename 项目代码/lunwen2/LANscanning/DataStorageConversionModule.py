import json
import socket
import PythonJson as DEMPJ
class PythonJsonConversion():
    RowCount = 0
    hostname = socket.gethostname()
    locallhost = socket.gethostbyname(hostname)
    def StagingList(self,target_addr,IcmpResult,name,symbol):#数据暂存列表
        PythonJsonConversion.RowCount=PythonJsonConversion.RowCount+1
        ListDataConverter={'RowCount':PythonJsonConversion.RowCount,
                            'LocallHost':PythonJsonConversion.locallhost,
                            'TargetAddr':target_addr,
                            'IcmpResult':IcmpResult,
                            'name': name,
                            'symbol':symbol
                            }
        DEMPJ.PythonJson.timeoutData.append(ListDataConverter)
        # with open('D:/pycharxiangmu/lunwen2/LANscanning/DataStagingModule/JsonFile/%s.json' % DEMPJ.PythonJson.JsonFileName , encoding='utf-8') as JF:
        #     json.dump(PythonJsonConversion.timeoutData,JF)

    def ListTransferredToJson(self):#list转入json

        p=DEMPJ.PythonJson()


        filepath='E:/论文/项目20229.21/lunwen2/LANscanning/DataStagingModule/%s.json' % p.JsonFileName

        # with open(filepath, 'w') as f:
        #     f.write('[')
        #     for value in DEMPJ.PythonJson.timeoutData:
        #
        #         f.write(json.dumps(value))
        #         f.write(','+'\n')
        #     f.write(']')
        #

        with open(filepath, 'w', encoding='utf-8') as JF:
            json.dump(DEMPJ.PythonJson.timeoutData,JF,indent=1)



