import json
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5 import QtWidgets,QtCore
from selenium.common.exceptions import NoSuchElementException

class CreateDataJsonToPyqtTree():
    ChildChuild = []
    def TreeSubject(self):
        # self.ChuilddockWidget = QtWidgets.QDockWidget('窗体', self)
        self.ChildTree = QTreeWidget()
        self.ChildTree.setColumnCount(1)
        self.ChildTree.setHeaderLabels(['IP'])
        self.ChildTree.setColumnWidth(0,200)
        self.ScannedDevices = QTreeWidgetItem(self.ChildTree)
        self.DevicesNotScanned = QTreeWidgetItem(self.ChildTree)
        self.CreateTreeNodeSuspensionWindowTree()
    def CreateTreeNodeSuspensionWindowTree(self):
        if CreateDataJsonToPyqtTree.ChildChuild:
            # for i in range(len(CreateTreeNodeSuspensionWindow.chuild)):
            #     # self.root = QTreeWidgetItem(self.tree)
            #     # python批量设置项目。试试字典。for循环下，dict[i]=QWxxx模块
            #     ceshiceshi=CreateTreeNodeSuspensionWindow.chuild[i]
            pass
            #####
            # self.ChildTree.clear()
            #
            # self.ChildWindow = QTreeWidgetItem(self.ChildTree)
            # self.ChildWindow.setText(0, '已打开子窗口')
            # self.gen_branch(self.ChildWindow, CreateDataJsonToPyqtTree.ChildChuild)
            #
            # self.tree.expandAll()
            # self.sub.setWidget(self.ChildTree)#查查命令是什么意思
            # self.sub.setFloating(False)
            # self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.sub)
        else:
            self.ScannedDevices.setText(0, 'Null')
            # self.ScannedDevices.setText(1, 'Null')
            self.DevicesNotScanned.setText(0, 'Null')
            # self.DevicesNotScanned.setText(1, 'Null')
            self.ChildTree.addTopLevelItem(self.ScannedDevices)
            self.ChildTree.addTopLevelItem(self.DevicesNotScanned)
            # self.sub.setCentralWidget(self.ChildTree)
            self.sub.setWidget(self.ChildTree)
            # self.sub.setFloating(False)
            # return self.ChildTree

            # self.sub.setWidget(QtWidgets.QTextEdit())
            # self.sub.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.ChuilddockWidget)