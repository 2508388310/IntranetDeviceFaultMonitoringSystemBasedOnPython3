from PyQt5.QtWidgets import *

from Interface.MainWindow import CreateActionEffects as CAE


# from CreateScanWindow import CreateScanWindow
# from CreateScanWindow import CreateScanWindow
# ,CAE.CAEchildWindowss
class Signal(CAE.CreateActionEffect,QMainWindow):


    def SCopenfile(self):
        self.openAction.triggered.connect(self.CAEopenfile)
    def SCexitMainWindow(self):
        self.exitAction.triggered.connect(self.CAEexitMainWindow)
    def SCnewScanWindow(self):
        pass
        # self.newAction.triggered.connect(self.CAEnewAction)

    def SCchildWindows(self):

        self.count = 0
        self.mdi = QMdiArea()

        # self.CAEchildWindows()
        self.newAction.triggered.connect(self.CAEchildWindows)
    # def X(self):
    #     try:
    #         self.setCentralWidget(self.mdi)
    #         self.sub = QMdiSubWindow()
    #         Signal.count = Signal.count + 1
    #
    #         self.sub.setWindowTitle("扫描" + str(Signal.count))
    #         self.sub.resize(300, 300)
    #
    #         # self.mdi.addSubWindow()
    #
    #         # self.mdi
    #         # sub.setWidget(PyQt5.QtWidgets.QFrame.)
    #         self.mdi.addSubWindow(self.sub)
    #         self.sub.show()
    #         # self.mdi.cascadeSubWindows()
    #         # CAEchildWindowsEffect.CAEchildWindowsEffect.CAEchildWindowsEffect(self)
    #     except Exception as e:
    #         print(e)
