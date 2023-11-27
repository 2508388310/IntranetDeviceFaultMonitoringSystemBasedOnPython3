import PyQt5.QtWidgets
from PyQt5.QtGui import QIcon
class CreateAction():
        def CreateToolBarAction(self):
                #CA创建，CMB和CTB调用
                #理想情况CA创建，把CMB和CTB用方法分开，重用的就可以相互调用，需要别的logo就拉到各自的py文件自己设置
                self.newAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/saomiao.svg'), "&New", self)
                # Creating actions using the second constructor
                self.openAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Open...", self)
                self.saveAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Save", self)
                self.exitAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Exit", self)
                self.copyAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/saomiao.svg'), "&Copy", self)
                self.pasteAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Paste", self)
                self.cutAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Cut", self)
                self.helpContentAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Help Content", self)
                self.aboutAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&About", self)
