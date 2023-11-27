
class CreateTabOptions():
    def __init__(self):
        self.tab1 = PyQt5.QtWidgets.QWidget()
        self.tab2 = PyQt5.QtWidgets.QWidgetQWidget()
        self.tab3 = PyQt5.QtWidgets.QWidgetQWidget()

        self.addTab(self.tab1, '选项卡1')
        self.addTab(self.tab2, '选项卡2')
        self.addTab(self.tab3, '选项卡3')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()



    def tab1UI(self):
        layout = PyQt5.QtWidgets.QFormLayout()
        layout.addRow('姓名', PyQt5.QtWidgets.QLineEdit())
        layout.addRow('地址', PyQt5.QtWidgets.QLineEdit())
        self.setTabText(0, '联系方式')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = PyQt5.QtWidgets.QHBoxLayout()
        sex.addWidget(PyQt5.QtWidgets.QRadioButton('男'))
        sex.addWidget(PyQt5.QtWidgets.QRadioButton('女'))
        layout.addRow(PyQt5.QtWidgets.QLabel('性别'), sex)
        layout.addRow('生日', PyQt5.QtWidgets.QLineEdit())
        self.setTabText(1, '个人详细信息')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = PyQt5.QtWidgets.QHBoxLayout()
        layout.addWidget(PyQt5.QtWidgets.QLabel('科目'))
        layout.addWidget(PyQt5.QtWidgets.QCheckBox('物理'))
        layout.addWidget(PyQt5.QtWidgets.QCheckBox('高数'))
        self.setTabText(2, '教育程度')
        self.tab3.setLayout(layout)