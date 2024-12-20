# Form implementation generated from reading ui file 'd:\mindx_app\app_intensive\project\SignupScreen.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 663)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.811, y1:0.948864, x2:0.910448, y2:0, stop:0.323383 rgba(204, 111, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.811, y1:0.948864, x2:0.910448, y2:0, stop:0.323383 rgba(204, 111, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(parent=self.frame)
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.frame_7)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/user-login-icon-14.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(500, 40))
        self.frame_6.setMaximumSize(QtCore.QSize(200, 100))
        self.frame_6.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(10000, 500))
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtUsername_2 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.txtUsername_2.setMinimumSize(QtCore.QSize(100, 30))
        self.txtUsername_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txtUsername_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.txtUsername_2.setObjectName("txtUsername_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtUsername_2)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtPassword_2 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.txtPassword_2.setMinimumSize(QtCore.QSize(100, 30))
        self.txtPassword_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;background-color: rgb(255, 255, 255);\n"
"")
        self.txtPassword_2.setClearButtonEnabled(True)
        self.txtPassword_2.setObjectName("txtPassword_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtPassword_2)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame_3)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.dateEdit)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame)
        self.frame_8.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Signup_button = QtWidgets.QPushButton(parent=self.frame_8)
        self.Signup_button.setMinimumSize(QtCore.QSize(60, 40))
        self.Signup_button.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Signup_button.setFont(font)
        self.Signup_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.Signup_button.setObjectName("Signup_button")
        self.horizontalLayout_5.addWidget(self.Signup_button)
        self.verticalLayout.addWidget(self.frame_8)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SIGN UP"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.txtUsername_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.txtPassword_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Birthday"))
        self.Signup_button.setText(_translate("MainWindow", "SIGN UP"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
