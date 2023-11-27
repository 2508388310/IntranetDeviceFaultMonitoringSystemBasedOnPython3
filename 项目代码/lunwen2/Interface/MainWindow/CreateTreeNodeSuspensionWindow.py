from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
import time
# from SignalConnection import Signal as S


class CreateTreeNodeSuspensionWindow():
    chuild = []
    def CreateTreeNodeSuspensionWindow(self,count=0):
        self.dockWidget = QtWidgets.QDockWidget('窗体监控', self)
        # label = QtWidgets.QLabel('TopDockWidgetArea')
        # self.dockWidget.setWidget(label)
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['窗体', '创建时间'])
        self.tree.setColumnWidth(200,400)
        # self.tree.setFixedWidth(200)
        self.OpenedWindow = QTreeWidgetItem(self.tree)
        # self.gen_branch()

        self.CreateTreeNodeSuspensionWindowTree()

    def CreateTreeNodeSuspensionWindowTree(self):
        if CreateTreeNodeSuspensionWindow.chuild:
            # for i in range(len(CreateTreeNodeSuspensionWindow.chuild)):
            #     # self.root = QTreeWidgetItem(self.tree)
            #     # python批量设置项目。试试字典。for循环下，dict[i]=QWxxx模块
            #     ceshiceshi=CreateTreeNodeSuspensionWindow.chuild[i]
            self.tree.clear()
            self.ChildWindow = QTreeWidgetItem(self.tree)
            self.ChildWindow.setText(0, '已打开子窗口')
            self.gen_branch(self.ChildWindow, CreateTreeNodeSuspensionWindow.chuild)

            self.tree.expandAll()
            self.dockWidget.setWidget(self.tree)#查查命令是什么意思
            self.dockWidget.setFloating(False)
            self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockWidget)
        else:
            self.OpenedWindow.setText(0, 'Null')
            self.OpenedWindow.setText(1, 'Null')
            self.dockWidget.setWidget(self.tree)
            self.dockWidget.setFloating(False)
            self.setCentralWidget(QtWidgets.QTextEdit())
            self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockWidget)

    def gen_branch(self,node: QTreeWidgetItem, texts:list):
        """ 给定某个节点和列表 在该节点生成列表内分支"""
        for text in texts:
            item = QTreeWidgetItem()
            item.setText(0, text)
            # item.setCheckState(0, Qt.Unchecked)
            item.setText(1, 'null')
            node.addChild(item)




