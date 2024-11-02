from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6 import uic
import re
import sys
import json
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SigninScreen.ui", self)
    def load_users(filename):
        with open(filename, 'r',) as file:
            data = json.load(file)
        return data['users']

# Function to check login credentials
    def login(users, username, password):
        for user in users:
            if user['username'] == username and user['password'] == password:
             return True
        return False
    def main(self, load_users, login):
        # Load users from the JSON file
        users = load_users('data/tai_khoan_nguoi_dung.json')

        # Ask for username and password
        username = self.txtname.text()
        password = self.txtPass.text()

        # Check login credentials
        if login(users, username, password):
            logupPage.close()
            mainPage.show()
        if not username:
            msg_box.setText("Vui lòng nhập Username!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        else:
            msg_box.setText("Login failed. Please check your username and password.")
            msg_box.exec()
            
class Logup(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__
        uic.loadUi("Signup_Screen_ui.ui", self)
        self.Signup_button.clicked.connect(self.check_logup)
    def check_logup(self):
        Username_1 = self.txtname.text()
        password_1 = self.txtPass.text()
        if not Username_1:
            msg_box.setText("Vui lòng nhập Username!")
            msg_box.exec()
            return
        if not password_1:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        else:
            self.close()
            loginPage.show()
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SigninScreen.ui", self)
    #     self.icon_pha_do_1.clicked.connect(self.pha_do_1)
    #     self.icon_pha_do_2.clicked.connect(self.pha_do_2)
    #     self.icon_pha_he_1.clicked.connect(self.pha_he_1) 
    #     self.icon_pha_he_2.clicked.connect(self.pha_he_2)
    #     self.icon_pha_ky_1.clicked.connect(self.pha_ky_1)
    #     self.icon_pha_ky_2.clicked.connect(self.pha_ky_2)      
    # def pha_do_1(self):
    #     pha_do_1.show()
    # def pha_do_2(self):
    #     pha_do_2.show()
    # def pha_he_1(self):
    #     pha_he_1.show()
    # def pha_he_2(self):
    #     pha_he_2.show()
    # def pha_ky_1(self):
    #     pha_ky_2.show()
    # def pha_ky_2(self):
    #     pha_ky_2.show()
        
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
    # logupPage = Logup()
    # mainPage = Main()
    # pha_do_1 = pd1()
    # pha_do_2 = pd2()
    # pha_he_1 = ph1()
    # pha_he_2 = ph2()
    # pha_ky_1 = pk1()
    # pha_ky_2 = pk2()
    # Thiết lập hộp thoại thông báo lỗi
    # msg_box = QMessageBox()
    # msg_box.setWindowTitle("Lỗi")
    # msg_box.setIcon(QMessageBox.Icon.Warning)
    # msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    app.exec()



