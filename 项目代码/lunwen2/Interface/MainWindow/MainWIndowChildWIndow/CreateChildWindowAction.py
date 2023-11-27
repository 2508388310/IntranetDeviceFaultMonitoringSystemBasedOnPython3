import PyQt5.QtWidgets
from PyQt5.QtGui import QIcon

class CreateChildACtion():
    def CreateChildWindowsToolBarACtion(self):
        self.searchAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/saomiao.svg'), "&New", self)
        # Creating actions using the second constructor
        self.stopAction =PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Open...", self)
        self.delectAction = PyQt5.QtWidgets.QAction(QIcon('../source_material/resources/exit.svg'), "&Save", self)
