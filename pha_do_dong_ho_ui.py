# Form implementation generated from reading ui file 'd:\mindx_app\app_intensive\project\pha_do_dong_ho.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 754)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.811, y1:0.948864, x2:0.910448, y2:0, stop:0.323383 rgba(204, 111, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        MainWindow.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 957, 100))
        self.frame.setMinimumSize(QtCore.QSize(100, 100))
        self.frame.setMaximumSize(QtCore.QSize(1000, 100))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame)
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
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(150, 100))
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
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame)
        self.frame_7.setMaximumSize(QtCore.QSize(150, 100))
        self.frame_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
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
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_7)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_phả_ kế.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(150, 100))
        self.frame_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.frame_8.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_8)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon-menu-đẹp.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 100))
        self.frame_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
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
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_9.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QWidget:hover{\n"
"\n"
"border-radius: 15px;\n"
"    background-color: rgb(236, 150, 30);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/png-clipart-computer-icons-git-branching-fork-git-share-icon-graphical-user-interface-thumbnail.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 120, 957, 100))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 767, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_trang_chu_gia_pha.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Gigi")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 270, 91, 31))
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 270, 131, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 270, 151, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(520, 270, 261, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 270, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 270, 41, 28))
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/Search_Icon.svg.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 310, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.frame_10 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(0, 350, 981, 50))
        self.frame_10.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_10.setStyleSheet("background-color: #977D41;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_8.setGeometry(QtCore.QRect(150, 10, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_10.setGeometry(QtCore.QRect(280, 10, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(410, 10, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_12.setGeometry(QtCore.QRect(530, 10, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 400, 957, 300))
        self.tableWidget.setMinimumSize(QtCore.QSize(100, 300))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setIconSize(QtCore.QSize(100, 100))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("d:\\mindx_app\\app_intensive\\project\\imgs/icon_sua.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(icon5)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon5)
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon5)
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon5)
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon5)
        self.tableWidget.setItem(4, 4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Trang Chủ"))
        self.pushButton_7.setText(_translate("MainWindow", "Phả Kế"))
        self.pushButton_6.setText(_translate("MainWindow", "Phả Hệ"))
        self.pushButton_9.setText(_translate("MainWindow", "Phả Đồ"))
        self.label_3.setText(_translate("MainWindow", "PHẢ ĐỒ DÒNG HỌ NGUYỄN"))
        self.label_4.setText(_translate("MainWindow", "Bộ lọc:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Tổ chi"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Tháng giỗ"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Sinh/ Mất"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Tên"))
        self.pushButton_2.setText(_translate("MainWindow", "Xóa lọc"))
        self.label_5.setText(_translate("MainWindow", "Danh sách thành viên"))
        self.label_8.setText(_translate("MainWindow", "Đời"))
        self.label_9.setText(_translate("MainWindow", "Tên"))
        self.label_10.setText(_translate("MainWindow", "Chi - Ngành - Nhánh"))
        self.label_11.setText(_translate("MainWindow", "Ngày"))
        self.label_12.setText(_translate("MainWindow", "Sửa thông tin"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Nguyễn Văn A"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Đời"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Chi - Ngành - Nhánh"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Sinh: dd/mm/yy  - Mất: dd/mm/yy"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Nguyễn Văn A"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Đời"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "Chi - Ngành - Nhánh"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "Sinh: dd/mm/yy  - Mất: dd/mm/yy"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Nguyễn Văn A"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "Đời"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "Chi - Ngành - Nhánh"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "Sinh: dd/mm/yy  - Mất: dd/mm/yy"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Nguyễn Văn A"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "Đời"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "Chi - Ngành - Nhánh"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "Sinh: dd/mm/yy  - Mất: dd/mm/yy"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Nguyễn Văn A"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "Đời"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "Chi - Ngành - Nhánh"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", "Sinh: dd/mm/yy  - Mất: dd/mm/yy"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
