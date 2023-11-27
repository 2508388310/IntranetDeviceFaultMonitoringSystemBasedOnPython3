import PyQt5.QtCore
import PyQt5.QtWidgets


class CreateMenuBar():
    #CMBFM全继承CA，CA里全都是self.newAction
    #或者CA多方法拆开，给不同不同文件继承CA的不同def
    def CreateMenuBar(self):
        # Setting contextMenuPolicy
        # self.centralWidget.setContextMenuPolicy(PyQt5.QtCore.Qt.ActionsContextMenu)
        # Populating the widget with actions
        # self.centralWidget.addAction(self.newAction)
        # self.centralWidget.addAction(self.openAction)
        # self.centralWidget.addAction(self.saveAction)
        # self.centralWidget.addAction(self.copyAction)
        # self.centralWidget.addAction(self.pasteAction)
        # self.centralWidget.addAction(self.cutAction)
        # menuBar = QMenuBar(self)
        # self.setMenuBar(menuBar)
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        File = PyQt5.QtWidgets.QMenu("&File", self)
        menuBar.addMenu(File)
        File.addAction(self.newAction)
        File.addAction(self.openAction)
        saveAction = File.addMenu("Save")#这个是有小菜单的
        saveAction.addAction("SaveTxt")#这里还是要携程self.的形式
        saveAction.addAction("SaveMysql")
        saveAction.addAction("SaveExcel")
        File.addSeparator()
        File.addAction(self.exitAction)

        ## Edit menu
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace...")
        ## Help menu
        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)