
import PyQt5.QtWidgets
import PyQt5.QtCore
import MainWindowEdit as MWE
import sys

from CreateAction import CreateAction as CA
from CreateMenuBar import CreateMenuBar as CMB
from CreateToolBar import CreateToolBar as CTB
# from CreateActionEffects import CreateActionEffects as CAE
import SignalConnection as SC
from CreateTreeNodeSuspensionWindow import CreateTreeNodeSuspensionWindow as CTNSW
# import CreateTabOptions as CTO
# import CreateScanWindow as CSW
# import CAEchildWindowsEffect as CAECWE
class MainWindow(MWE.MainWindowEdit,SC.Signal,CA,CMB,CTB,CTNSW):
    def __init__(self):
        super().__init__()
        # MWE.MainWindowEdit(self)
        # self.createActions()  # 注意顺序问题
        CA.CreateToolBarAction(self)
        CMB.CreateMenuBar(self)#菜单
        # CAECWE.CAEchildWindowsEffect()




        CTB.CreateToolBar(self)#工具栏
        # SC.Signal.SCchildWindows(self)
        SC.Signal.SCexitMainWindow(self)
        SC.Signal.SCopenfile(self)
        SC.Signal.SCnewScanWindow(self)
        SC.Signal.SCchildWindows(self)



        #信号槽
        CTNSW.CreateTreeNodeSuspensionWindow(self)

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
