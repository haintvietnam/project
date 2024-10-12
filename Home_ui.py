# Form implementation generated from reading ui file 'd:\mindx_app\app_intensive\project\Home.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 797)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.811, y1:0.948864, x2:0.910448, y2:0, stop:0.323383 rgba(204, 111, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(parent=self.page)
        self.frame_5.setMaximumSize(QtCore.QSize(100, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(5, 5))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.page)
        self.frame_6.setMaximumSize(QtCore.QSize(200, 100))
        self.frame_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.frame_6.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.frame = QtWidgets.QFrame(parent=self.page)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_9.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/png-clipart-computer-icons-git-branching-fork-git-share-icon-graphical-user-interface-thumbnail.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.horizontalLayout_5.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(parent=self.page)
        self.frame_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_4.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pha_he_1 = QtWidgets.QPushButton(parent=self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon-menu-đẹp.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pha_he_1.setIcon(icon2)
        self.pha_he_1.setIconSize(QtCore.QSize(35, 35))
        self.pha_he_1.setObjectName("pha_he_1")
        self.horizontalLayout.addWidget(self.pha_he_1)
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.frame_7 = QtWidgets.QFrame(parent=self.page)
        self.frame_7.setMaximumSize(QtCore.QSize(200, 100))
        self.frame_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.frame_7.setToolTipDuration(-3)
        self.frame_7.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pha_ky_1 = QtWidgets.QPushButton(parent=self.frame_7)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_phả_ kế.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pha_ky_1.setIcon(icon3)
        self.pha_ky_1.setObjectName("pha_ky_1")
        self.horizontalLayout_3.addWidget(self.pha_ky_1)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 160))
        self.frame_2.setMaximumSize(QtCore.QSize(1000, 400))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 671, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_trang_chu_gia_pha.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Gigi")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_3.setMaximumSize(QtCore.QSize(1000, 450))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pha_do_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pha_do_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pha_do_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_phả_đồ.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pha_do_2.setIcon(icon4)
        self.pha_do_2.setIconSize(QtCore.QSize(500, 500))
        self.pha_do_2.setObjectName("pha_do_2")
        self.verticalLayout.addWidget(self.pha_do_2)
        self.pha_ky_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pha_ky_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pha_ky_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/iocn_1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pha_ky_2.setIcon(icon5)
        self.pha_ky_2.setIconSize(QtCore.QSize(500, 500))
        self.pha_ky_2.setObjectName("pha_ky_2")
        self.verticalLayout.addWidget(self.pha_ky_2)
        self.pha_he_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pha_he_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pha_he_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_phả_hệ.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pha_he_2.setIcon(icon6)
        self.pha_he_2.setIconSize(QtCore.QSize(500, 500))
        self.pha_he_2.setObjectName("pha_he_2")
        self.verticalLayout.addWidget(self.pha_he_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Trang Chủ"))
        self.pushButton_9.setText(_translate("MainWindow", "Phả Đồ"))
        self.pha_he_1.setText(_translate("MainWindow", "Phả Hệ"))
        self.pha_ky_1.setText(_translate("MainWindow", "Phả Ký"))
        self.label_3.setText(_translate("MainWindow", "GIA PHẢ DÒNG HỌ NGUYỄN"))
