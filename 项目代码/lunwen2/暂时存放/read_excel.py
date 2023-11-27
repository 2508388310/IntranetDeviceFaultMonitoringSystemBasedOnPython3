import xlrd
from 暂时存放 import excel_mysql

path=r"C:\Users\Administrator.WIN-UDA4FC4QOHS\Desktop\测试病毒库.xlsx"
data = xlrd.open_workbook(path)
sheet_name='Sheet1'
table = data.sheet_by_name(sheet_name)		#通过名称获取
nrows = table.nrows
count=0


for i in range(0, 7):#行
    d = []
    if count==0:
        for a in range(1, 7):  # 列
            d.append(table.cell_value(i, a))
        count+=1
        print(d)


        # ac = d.split(',')
        # print(ac)
        excel_mysql.db_connect(a=d)
    else:
        for a in range(1,7):#列
            d.append(table.cell_value(i, a))
        # ac = d.split(',')
        print(d)
        excel_mysql.insert_data(data=d)











# for i in range(2,4):
#
#     print(c[i])
# name_list = [str() ]
# print("第4列所有的值：",name_list)
# for i in table.row(table.nrows):
#
#     print(i)
