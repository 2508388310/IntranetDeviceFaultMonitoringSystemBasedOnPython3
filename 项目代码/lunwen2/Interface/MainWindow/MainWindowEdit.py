import PyQt5.QtWidgets
from PyQt5.QtGui import QIcon


class MainWindowEdit(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindowLogo()
        # self.setIconSize(QIcon(36, 36))
        self.setWindowTitle("LanScanner")
        self.resize(1200, 900)
        # CreateTabOptions.CreateTabOptions(self)
    def MainWindowLogo(self):
        self.setWindowIcon(QIcon('../source_material/resources/logo.svg'))








