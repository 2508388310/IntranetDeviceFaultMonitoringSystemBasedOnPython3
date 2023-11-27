# import sys
# from PyQt5 import QtWidgets,QtCore
# app=QtWidgets.QApplication(sys.argv)
# widget=QtWidgets.QWidget()
# widget.resize(360,360)
# widget.setWindowTitle("hello,pyqt5")
# widget.show()
# sys.exit(app.exec_())
# dss='hello pyqt5'
# # print('dss',dss)
# zlst=('hello','PyQt5','.','com')
# vlst=('Top','Quant','.','vip')
# print('zlst,',zlst)
# print('vlst,',vlst)
# from ceshi13 import ceshi13
# class ceshi12 (ceshi13):
#     def __init__(self):
#         self.a=1
#         print("a")
#         self.b = 2
#         self.c = 3
#         self.a()
#         self.me()
#     def me(self):
#         print("c")
#         return self.c


'''

容纳多文档的窗口

QMdiArea

QMdiSubWindow

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)
        self.setWindowTitle("容纳多文档的窗口")




        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.TopToolBar = self.addToolBar("ChildWindowTopToolBar")  # 把bar加入mainwin
        self.TopToolBar.setFixedHeight(40)
        sub.setWidget(self.TopToolBar)




        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered.connect(self.windowaction)
    def windowaction(self,q):
        print(q.text())
        if q.text() == "New":

            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))

            # self.TopToolBar = self.addToolBar("ChildWindowTopToolBar")  # 把bar加入mainwin
            # self.TopToolBar.setFixedHeight(40)
            #
            # sub.setWidget(self.TopToolBar)




            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MultiWindows()
    demo.show()
    sys.exit(app.exec_())