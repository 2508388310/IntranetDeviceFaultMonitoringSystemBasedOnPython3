# import PyQt5
# from SignalConnection import Signal
# from PyQt5.QtCore import Qt
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *  # 导入浏览器的包
from PyQt5.QtWidgets import *
from pyqt5_plugins.examplebutton import QtWidgets

from CreateChildWindowLeftToolBar import CreateChildWindowLeftToolBars as CCWLTB
from CreateChildWindowsSignalConnection import ChildSignalConnection as CSC
from CreateTreeNodeSuspensionWindow import CreateTreeNodeSuspensionWindow as CTNSW

sys.path.append(r'E:\论文\项目20229.21\lunwen2\LANscanning')
from JsonConverter.DataJsonToPyqtTree import CreateDataJsonToPyqtTree as CDJTPT
import DataExchangeModule.PythonJson as DEMPJ
class CreateChildWindow(QMainWindow):
    def CreateChildWindowMainWindow(self):
        self.setCentralWidget(self.mdi)
        self.sub = QMdiSubWindow()
        #
        self.web_view = QWebEngineView()

        #

        self.count = self.count + 1
        DEMPJ.PythonJson()
        JsonFileName=DEMPJ.PythonJson()#注意有没有()

        # DEMPJ.PythonJson.JsonFileName = DEMPJ.PythonJson()
        CreateChildWindowMainWindowName="扫描" + str(self.count)+"---"+JsonFileName.JsonFileName
        self.sub.setWindowTitle(CreateChildWindowMainWindowName)
        CTNSW.chuild.append(CreateChildWindowMainWindowName)
        CTNSW.CreateTreeNodeSuspensionWindowTree(self)


        self.sub.resize(600, 600)
        self.ChildWindowleftToolBar = QToolBar("ChildWindowRightToolBar")



        # self.ChuilddockWidget = QDockWidget('窗体', self)



##

        # self.centralwidget = QtWidgets.QWidget(QMdiSubWindow)
        # # self.centralwidget.setObjectName("centralwidget")
        #
        #
        # # from PyQt5.QtWebEngineWidgets import *  # 导入浏览器的包
        # self.webView = QWebEngineView(self.centralwidget)
        # # (左边离窗口距离, 右边离窗口距离, 浏览器的宽度, 浏览器的高度)
        # self.webView.setGeometry(QtCore.QRect(50, 50, 50, 50))  # (50 左边, 50 右边, 700 宽, 500 高)
        # # 设置浏览器的默认地址
        # self.webView.setUrl(QtCore.QUrl("https://www.baidu.com/"))
        # # self.webView.setObjectName("浏览器")
        # QMdiSubWindow.
        #
        # # self.browser = QWebEngineView()
        # # # 加载外部的web界面
        # # self.browser.load(QUrl('https://www.baidu.com'))
        # # self.setCentralWidget(self.browser)



        #web_view.load(QUrl("https://www.baidu.com"))

        ##
        CCWLTB.CreateChildWindowLeftToolBarss(self)

        CSC.CSCsearch(self)
        CDJTPT.TreeSubject(self)
        # ####
        # self.ChildTree = QTreeWidget()
        # self.ChildTree.setColumnCount(1)
        # self.ChildTree.setHeaderLabels(['IP'])
        # self.ChildTree.setColumnWidth(200, 200)
        # self.ScannedDevices = QTreeWidgetItem(self.ChildTree)
        # self.DevicesNotScanned = QTreeWidgetItem(self.ChildTree)
        #
        # self.ScannedDevices.setText(0, 'Null')
        # # self.ScannedDevices.setText(1, 'Null')
        # self.DevicesNotScanned.setText(0, 'Null')
        # # self.DevicesNotScanned.setText(1, 'Null')
        # self.ChildTree.addTopLevelItem(self.ScannedDevices)
        # self.ChildTree.addTopLevelItem(self.DevicesNotScanned)
        # # self.sub.setCentralWidget(self.ChildTree)
        # self.sub.setWidget(self.ChildTree)
        #########

        self.sub.setWidget(self.ChildWindowleftToolBar)
        # self.sub.addAction(self.ChildWindowleftToolBar)
        self.sub.setWidget(self.web_view)
        #
        #self.subweb.setWidget(self.web_view)
        #


        # self.mdi.addSubWindow()
        # self.mdi
        # sub.setWidget(PyQt5.QtWidgets.QFrame.)
        self.mdi.addSubWindow(self.sub)
        #

        #
        self.sub.show()
        self.web_view.load(QUrl("http://localhost:8601/"))



