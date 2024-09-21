from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6 import uic
import re
import sys
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SigninScreen.ui", self)
        self.Signin_button.clicked.connect(self.check_login)
        # self.btn_register.clicked.connect(self.showRegister)
    def check_login(self):
        Username = self.txtUsername.text()
        password = self.txtPassword.text()
        if not Username: 
            msg_box.setText("Vui lòng nhập Username hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        if Username == "admin@example.com" and password == "admin":
            self.close()
            mainPage.show()  
        else:
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test_mindx.ui", self)
        self.icon_stn.clicked.connect(self.sach_thieu_nhi)
        self.btn_opt_stn.clicked.connect(self.sach_thieu_nhi)
        self.icon_stk.clicked.connect(self.sach_tham_khao)
        self.btn_opt_stk.clicked.connect(self.sach_tham_khao)
        self.icon_skt.clicked.connect(self.sach_kinh_te) 
        self.btn_opt_skt.clicked.connect(self.sach_kinh_te)
        self.icon_svh.clicked.connect(self.sach_van_hoc)
        self.btn_opt_svh.clicked.connect(self.sach_van_hoc)      
    def sach_thieu_nhi(self):
        sach_thieu_nhi.show()
    def sach_tham_khao(self):
        sachthamkhao.show()
    def sach_kinh_te(self):
        sachkinhte.show()
    def sach_van_hoc(self):
        sach_van_hoc.show()
        
class SachThieuNhi(QtWidgets.QMainWindow):
    def __init__(self):
        super(SachThieuNhi,self).__init__()
        pagename = "sach_thieu_nhi.ui"
        uic. loadUi (pagename, self)
        self.btn_back.clicked.connect(self.close)
        self.btn_close.clicked.connect(self.close)
        
    def sach_thieu_nhi(self):
        sach_thieu_nhi.show()    
        mainPage.close()
        self.close()
class SachThamKhao(QtWidgets.QMainWindow):
    def __init__(self):
        super(SachThamKhao,self).__init__()
        pagename = "sach_thieu_nhi(1).ui"
        uic. loadUi (pagename, self)
        self.btn_back.clicked.connect(self.close)
        self.btn_close.clicked.connect(self.close)
class SachKinhTe(QtWidgets.QMainWindow):
    def __init__(self):
        super(SachKinhTe,self).__init__()
        pagename = "sach_kinh_te.ui"
        uic. loadUi (pagename, self)
        self.btn_back.clicked.connect(self.close)
        self.btn_close.clicked.connect(self.close)
class SachVanHoc(QtWidgets.QMainWindow):
    def __init__(self):
        super(SachVanHoc,self).__init__()
        pagename = "sach_van_hoc(1).ui"
        uic.loadUi (pagename, self)
        self.btn_back.clicked.connect(self.close)
        self.btn_close.clicked.connect(self.close)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #Tạo các đối tượng tương ứng với các trang giao diện
    loginPage = Login()
    loginPage.show()
    mainPage = Main()
    sach_thieu_nhi = SachThieuNhi()
    sachthamkhao = SachThamKhao()
    sachkinhte = SachKinhTe()
    sach_van_hoc = SachVanHoc()
    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    app.exec()
