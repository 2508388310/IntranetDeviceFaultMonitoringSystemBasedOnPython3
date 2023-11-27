from  PyQt5.QtWidgets import *

# from SignalConnection import count

# class CreateActionEffectsCount():
#     CreateActionEffectsCount = 0


from ScanWindow import CreateScanWindow
from Interface.MainWindow.MainWIndowChildWIndow.CreateChildWindows import CreateChildWindow as CCW

from Interface.MainWindow.MainWIndowChildWIndow.CreateChildWindowAction import CreateChildACtion  as ceshi


class CreateActionEffect():
    # CreateActionEffectsCount = 0
    # def __init__(self):
    #     self.CAEnewAction()
    #     self.CAEexitMainWindow()
    #     self.CAEopenfile()
    def CAEexitMainWindow(self):
        self.exitMainWindow=QApplication.instance()
        self.exitMainWindow.quit()
    def CAEopenfile(self):
        QFileDialog.getOpenFileName(self, '打开', './')
    def CAEnewAction(self):
        # appc = PyQt5.QtWidgets.QApplication(sys.argv)
        self.a = CreateScanWindow()
        self.a.show()
        # return CreateScanWindow(self)
        # winxx.show
        # sys.exit(appc.exec_())
    def CAEchildWindows(self):
        # self.count = self.count + 1
        # sub = QMdiSubWindow()
        # sub.setWindowTitle("扫描" + str(self.count))
        # sub.resize(300, 300)
        # self.mdi.cascadeSubWindows(sub)
        # sub.show()
        # print('b')
        #
        # self.newAction.triggered.connect(self.X)
        ceshi.CreateChildWindowsToolBarACtion(self)
        CCW.CreateChildWindowMainWindow(self)














