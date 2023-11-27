import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
class CreateChildWindowLeftToolBars():
    def CreateChildWindowLeftToolBarss(self):
          # 产生bar
        self.addToolBar(Qt.LeftToolBarArea, self.ChildWindowleftToolBar)  # 把bar加入mainwin
        self.ChildWindowleftToolBar.setFixedHeight(150)
        self.ChildWindowleftToolBar.setFixedWidth(50)
        # self.TopToolBar=self.addToolBar("ChildWindowTopToolBar")  # 把bar加入mainwin
        # self.TopToolBar.setFixedHeight(40)
        self.ChildWindowleftToolBar.addAction(self.searchAction)
        self.ChildWindowleftToolBar.addAction(self.stopAction)
        self.ChildWindowleftToolBar.addAction(self.delectAction)

