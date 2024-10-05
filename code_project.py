from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6 import uic
import re
import sys
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pha_do_dong_ho.ui", self)
        # self.Signin_button.clicked.connect(self.check_login)
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
        uic.loadUi("pha_do_dong_ho.ui", self)
#         self.icon_pha_do_1.clicked.connect(self.pha_do_1)
#         self.icon_pha_do_2.clicked.connect(self.pha_do_2)
#         self.icon_cong_duc_1.clicked.connect(self.cong_duc_1)
#         self.icon_cong_duc_2.clicked.connect(self.cong_duc_2)
#         self.icon_pha_he_1.clicked.connect(self.pha_he_1) 
#         self.icon_pha_he_2.clicked.connect(self.pha_he_2)
#         self.icon_pha_ky_1.clicked.connect(self.pha_ky_1)
#         self.icon_pha_ky_2.clicked.connect(self.pha_ky_2)      
#     def pha_do_1(self):
#         pha_do_1.show()
#     def pha_do_2(self):
#         pha_do_2.show()
#     def cong_duc_1(self):
#         cong_duc_1.show()
#     def cong_duc_2(self):
#         cong_duc_2.show()
#     def pha_he_1(self):
#         pha_he_1.show()
#     def pha_he_2(self):
#         pha_he_2.show()
#     def pha_ky_1(self):
#         pha_he_2.show()
#     def pha_ky_2(self):
#         pha_he_2.show()
        
# class ph1(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(ph1,self).__init__()
#         pagename = ".ui"
#         uic. loadUi (pagename, self)
#         self.btn_back.clicked.connect(self.close)
#         self.btn_close.clicked.connect(self.close)
        
#     def p_h_1(self):
#         pha_he_1.show()    
#         mainPage.close()
#         self.close()
# class ph2(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(ph2,self).__init__()
#         pagename = "sach_thieu_nhi(1).ui"
#         uic. loadUi (pagename, self)
#         self.btn_back.clicked.connect(self.close)
#         self.btn_close.clicked.connect(self.close)
# class SachKinhTe(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(SachKinhTe,self).__init__()
#         pagename = "sach_kinh_te.ui"
#         uic. loadUi (pagename, self)
#         self.btn_back.clicked.connect(self.close)
#         self.btn_close.clicked.connect(self.close)
# class SachVanHoc(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(SachVanHoc,self).__init__()
#         pagename = "sach_van_hoc(1).ui"
#         uic.loadUi (pagename, self)
#         self.btn_back.clicked.connect(self.close)
#         self.btn_close.clicked.connect(self.close)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
#     #Tạo các đối tượng tương ứng với các trang giao diện
    loginPage = Login()
    loginPage.show()
    mainPage = Main()
#     pha_do_1 = pd1()
#     pha_do_2 = pd2()
#     pha_he_1 = ph1()
#     pha_he_2 = ph2()
#     pha_ky_1 = pk1()
#     pha_ky_2 = pk2()
#     cong_duc_1 = cd1()
#     cong_duc_2 = cd2()
    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    app.exec()



