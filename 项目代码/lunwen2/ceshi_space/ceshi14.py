# '''
#
# 选项卡控件：QTabWidget
#
#
#
# '''
#
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class TabWidgetDemo(QTabWidget):
#     def __init__(self, parent=None):
#         super(TabWidgetDemo, self).__init__(parent)
#
#         self.setWindowTitle("选项卡控件：QTabWidget")
#         # 创建用于显示控件的窗口
#         self.tab1 = QWidget()
#         self.tab2 = QWidget()
#         self.tab3 = QWidget()
#
#         self.addTab(self.tab1,'选项卡1')
#         self.addTab(self.tab2,'选项卡2')
#         self.addTab(self.tab3,'选项卡3')
#
#         self.tab1UI()
#         self.tab2UI()
#         self.tab3UI()
#
#     def tab1UI(self):
#         layout = QFormLayout()
#         layout.addRow('姓名',QLineEdit())
#         layout.addRow('地址',QLineEdit())
#         self.setTabText(0,'联系方式')
#         self.tab1.setLayout(layout)
#
#     def tab2UI(self):
#         layout = QFormLayout()
#         sex = QHBoxLayout()
#         sex.addWidget(QRadioButton('男'))
#         sex.addWidget(QRadioButton('女'))
#         layout.addRow(QLabel('性别'),sex)
#         layout.addRow('生日',QLineEdit())
#         self.setTabText(1,'个人详细信息')
#         self.tab2.setLayout(layout)
#
#     def tab3UI(self):
#         layout = QHBoxLayout()
#         layout.addWidget(QLabel('科目'))
#         layout.addWidget(QCheckBox('物理'))
#         layout.addWidget(QCheckBox('高数'))
#         self.setTabText(2,'教育程度')
#         self.tab3.setLayout(layout)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = TabWidgetDemo()
#     demo.show()
#     sys.exit(app.exec_())


# class Root(object):
#     def __init__(self):
#         self.x = '这是属性'
#
#     def fun(self):
#         print(self.x)
#         print('这是方法')
#
#
# class A(Root):
#     def __init__(self):
#         super(A,self).__init__()
#         print('实例化时执行')
#
#
# test = A()  # 实例化类
# test.fun()  # 调用方法
# # test.x  # 调用属性
# from PyQt5.QtWidgets import QMainWindow
# from UI.index import Ui_MainWindow
#
# class MainWindow(QMainWindow,Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         self.setupUi(self)
#     def Query(self):
#         print('点击')
#         q.show()
# class QueryResul(QMainWindow,Ui_Query):
#
import sys

from PyQt5.QtCore import Qt
import PyQt5
from pyqt5_plugins.examplebutton import QtWidgets


class ceshi():
    def __init__(self):

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setAlignment(Qt.AlignCenter)

        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setMinimumSize(PyQt5.QtCore.QSize(500, 600))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox)
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = ceshi()
    win.show()
    sys.exit(app.exec_())