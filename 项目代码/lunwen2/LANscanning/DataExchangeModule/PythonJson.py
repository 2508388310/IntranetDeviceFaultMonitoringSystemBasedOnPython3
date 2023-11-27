import json
import datetime

class PythonJson():
    timeoutData = []
    #json文件名暂存
    def __init__(self):
        self.JsonFileName = ''
        self.CreatePythonJson()
        # print(PythonJson.JsonFileName)


    def CreatePythonJson(self):
        jsontime = PythonJson.CreateTime(self)
        FileName = 'json_{0}'.format(jsontime)
        seizeaseat=''
        # CreatePythonJsonFile=open('../DataStagingModule/JsonFile/%s.json' % time,'w')
        json.dump(seizeaseat,open('E:/论文/项目20229.21/lunwen2/LANscanning/DataStagingModule/JsonFile/%s.json' % FileName,'w'))
        self.JsonFileName=str(FileName)
        # CreatePythonJsonFile.close()

        # return FileName
    def CreateTime(self):
        return datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
if __name__ == "__main__":
    PythonJson()



