import PyQt5.QtWidgets
class CreateToolBar():
    def CreateToolBar(self):
        # Using a title
        # fileToolBar = self.addToolBar("File")
        # Using a QToolBar object
        # editToolBar = PyQt5.QtWidgets.QToolBar("Edit", self)
        # self.addToolBar(editToolBar)
        # Using a QToolBar object and a toolbar area
        self.LeftToolBar = PyQt5.QtWidgets.QToolBar("LeftToolBar", self)#产生bar
        self.addToolBar(PyQt5.QtCore.Qt.LeftToolBarArea, self.LeftToolBar)#把bar加入mainwin
        self.LeftToolBar.setFixedWidth(30)
        self.LeftToolBar.addAction(self.newAction)
        self.LeftToolBar.addAction(self.openAction)
        self.LeftToolBar.addAction(self.saveAction)
        self.LeftToolBar.addAction(self.copyAction)
        self.LeftToolBar.addAction(self.pasteAction)
        self.LeftToolBar.addAction(self.cutAction)
