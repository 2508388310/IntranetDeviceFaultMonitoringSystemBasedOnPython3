import sys

import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QMdiArea, QMdiSubWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建MDI区域
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 创建子窗口并添加到MDI区域
        sub_window = QMdiSubWindow()
        web_view = QWebEngineView()
        sub_window.setWidget(web_view)
        self.mdi_area.addSubWindow(sub_window)

        # 设置子窗口属性和内容
        sub_window.setWindowTitle("Embedded Browser")
        web_view.load(QUrl("http://localhost:8601"))
        sub_window.show()
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())