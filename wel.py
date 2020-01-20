import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from slots import Ui_MainWindow
class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi()

    def next(self):
        while True:
            self.obj= Ui_MainWindow()
            self.obj.show()

    def setupUi(self):
        welcome.setObjectName("welcome")
        welcome.resize(802, 434)
        self.label = QtWidgets.QLabel(welcome)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../park - Copy.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(welcome)
        self.pushButton.setGeometry(QtCore.QRect(320, 360, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.next)

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        _translate = QtCore.QCoreApplication.translate
        welcome.setWindowTitle(_translate("welcome", "Form"))
        self.pushButton.setText(_translate("welcome", "WELCOME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome = QtWidgets.QWidget()
    ui = Main()
    ui.setupUi()
    welcome.show()
    sys.exit(app.exec_())

