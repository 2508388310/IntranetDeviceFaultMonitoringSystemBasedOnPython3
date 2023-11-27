# import queue
#
# workqueue=queue.Queue(10)
# exit_flag=0
# for i in range(1,7):
#     workqueue.put(i)
# while exit_flag==0:
#     if workqueue.empty():
#         exit_flag = 1
#         print("空空空空空空空空空")
#     else:
#         for i in range(1,3):
#             a=workqueue.get()
#         print("第一组")
# print('结束')



# import http.client
#
# httpClient = http.client.HTTPConnection('192.168.31.171',65533)
# # 发送请求，直接用参数/，相当于直接访问ip+端口号
# httpClient.request('GET','/')
# # 获取请求
# response = httpClient.getresponse()
# # 分解response回应消息
# print("status:"+str(response.status))
# # print(response.reason)
# # print(response.read())
# print('-'*5+'Headers'+'-'*5)
# print(response.getheaders())
# print('-'*5+'Message'+'-'*5)
# print(response.msg)
import PyQt5.QtWidgets as s
import self as self
from PyQt5.QtCore import Qt
import PyQt5.QtCore as ss


class cc():
    def __init__(self):
        try:
            self.gridLayout = s.QGridLayout()
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setObjectName("gridLayout")
            self.gridLayout.setAlignment(Qt.AlignCenter)

            self.groupBox = s.QGroupBox()
            self.groupBox.setMinimumSize(ss.QSize(500, 600))
            self.groupBox.setObjectName("groupBox")
            self.gridLayout.addWidget(self.groupBox)
        except Exception as e:
            print(e)

cc()





