import sys
import PyQt5.QtWidgets
class CreateScanWindow(PyQt5.QtWidgets.QMainWindow):

    try:

        def __init__(self):
            super().__init__()
            self.xxxx()
        def xxxx(self):

            self.setWindowTitle("Lan")
            self.resize(400, 300)

    except Exception as a:
        print(a)




# if __name__ == '__main__':
#     # app = PyQt5.QtWidgets.QApplication(sys.argv)
#     win = CreateScanWindow()
#     # win.show()
#     # sys.exit(app.exec_())

