import pandas,json
class pandaswork():
    def ceshi(self):
        file = open('D:\pycharxiangmu\lunwen2\LANscanning\DataStagingModule\JsonFile\json_2022.09.20.20.59.27.json', 'r', encoding='utf-8')
        test = json.load(file)
        ceshi=pandas.DataFrame(test)
        #ceshi=pandas.read_json("D:\pycharxiangmu\lunwen2\LANscanning\DataStagingModule\JsonFile")
        pandas.set_option('display.max_columns', 6)  # 最多显示5列
        pandas.set_option('display.width', 100)
        a=ceshi[ceshi['symbol'] == 1]
        b=a["TargetAddr"].value_counts()#对b进行建树
        print(b)


if __name__ == '__main__':
    pandaswork().ceshi()