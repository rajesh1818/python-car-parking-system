from PyQt5 import QtCore, QtGui, QtWidgets
from register import Ui_Register
from T_login import *
import pymysql


class Ui_log(object):
    def openwindow(self):
        self.T_login = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setup3(self.T_login)
        self.T_login.show()


    def opwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_T_login()
        self.ui.setup2(self.window)
        self.window.show()




    def messagebox111(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()


    def messagebox1111(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

        self.opwindow()

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def login(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        conn=pymysql.connect(host="localhost",user="root",password="123456",db="customer")
        cur=conn.cursor()
        query="select * from login where username=%s and password=%s"
        data=cur.execute(query,(username,password))
        if(username=="admin" and password=="admin"):

            self.messagebox111("Successful", "LOGIN:Successful")
        elif(len(cur.fetchall())>0):

            self.messagebox1111("Successful","LOGIN:Successful")

        else:
            self.warning("Alert!","CHECK USERNAME OR PASSWORD")


    def setup1(self, log):
        log.setObjectName("log")
        log.resize(722, 479)
        self.label_2 = QtWidgets.QLabel(log)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(55)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(log)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(log)
        self.lineEdit.setGeometry(QtCore.QRect(270, 180, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(log)
        self.label_4.setGeometry(QtCore.QRect(50, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(log)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 270, 171, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(log)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 330, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.login)

        self.label_5 = QtWidgets.QLabel(log)
        self.label_5.setGeometry(QtCore.QRect(160, 400, 155, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(log)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 741, 481))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("blue1.png"))
        self.label_6.setObjectName("label_6")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(log)
        self.commandLinkButton.setGeometry(QtCore.QRect(315, 390, 221, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.opwindow)
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()

        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.commandLinkButton.raise_()

        self.retranslateUi(log)
        QtCore.QMetaObject.connectSlotsByName(log)

    def retranslateUi(self, log):
        _translate = QtCore.QCoreApplication.translate
        log.setWindowTitle(_translate("log", "log"))
        self.label_2.setText(_translate("log", "🔒LOGIN"))
        self.label_3.setText(_translate("log", "Username:"))
        self.label_4.setText(_translate("log", "Password:"))

        self.pushButton_2.setText(_translate("log", "Login"))
        self.label_5.setText(_translate("log", "Not Registered?"))
        self.commandLinkButton.setText(_translate("log", "CLICK HERE TO REGISTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    log = QtWidgets.QWidget()
    ui = Ui_log()
    ui.setup1(log)
    log.show()
    sys.exit(app.exec_())

