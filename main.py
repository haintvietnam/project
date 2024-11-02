import sys
import json
from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QMainWindow
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QColor, QPainter, QBrush
from PyQt6.uic import loadUi

class LoginSignUpWindow(QMainWindow):
    def __init__(self):
        super(LoginSignUpWindow, self).__init__()
        loadUi("SigninScreen.ui", self)
        self.Signin_button.clicked.connect(self.LoggingIn)

    def LoggingIn(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        
        def load_users(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
            return data['users']

        users = load_users('data/tai_khoan_nguoi_dung.json')

        def login(users, username, password):
            for user in users:
                if user['username'] == username and user['password'] == password:
                    return True
            return False

        if login(users, username, password):
            print("Authentication successful, opening next window...")
            self.MainWindow()
        else:
            print("Authentication failed, please try again.")

    def MainWindow(self):
        self.close()
        self.main_window = FamilyTreeWindow()
        self.main_window.show()

class FamilyTreeWindow(QMainWindow):
    def __init__(self):
        super(FamilyTreeWindow, self).__init__()
        loadUi("Home.ui", self)
        self.btnPhaHe.clicked.connect(self.NewWindow)

    def NewWindow(self):
        # self.close()
        self.main_window = PhaHeWindow()
        self.main_window.show()

# Load JSON data
with open("data/family_tree.json", "r", encoding="utf-8") as file:
    family_data = json.load(file)["data"]

def get_children(parent_id):
    return [member for member in family_data if member["bo"] == parent_id or member["me"] == parent_id]

class PhaHeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Family Tree")
        self.setGeometry(100, 100, 800, 600)

        self.graphics_view = QGraphicsView(self)
        self.setCentralWidget(self.graphics_view)

        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.draw_family_tree()

    def draw_family_tree(self):
        root_member = family_data[0]
        self.draw_member(root_member, QPointF(400, 20), 0)

    def draw_member(self, member, position, generation):
        color = QColor(173, 216, 230) if member["gioi_tinh"] == "nam" else QColor(255, 182, 193)

        node_radius = 30
        ellipse = QGraphicsEllipseItem(position.x() - node_radius, position.y(), node_radius * 2, node_radius * 2)
        ellipse.setBrush(QBrush(color))
        ellipse.setPen(QPen(Qt.GlobalColor.black, 2))
        self.scene.addItem(ellipse)

        name_text = QGraphicsTextItem(member["ten"])
        name_text.setPos(position.x() - node_radius / 2, position.y() + node_radius * 0.5)
        self.scene.addItem(name_text)

        ellipse.setToolTip(f"Name: {member['ten']}\nAge: {member['tuoi']}\nBirth Date: {member['ngay_sinh']}\nDeath Date: {member['ngay_mat']}")

        children = get_children(member["id"])
        y_offset = 100
        for i, child in enumerate(children):
            child_position = QPointF(position.x() + (i - len(children) / 2) * 150, position.y() + y_offset)
            line = QGraphicsLineItem(position.x(), position.y() + node_radius * 2,
                                     child_position.x(), child_position.y())
            line.setPen(QPen(Qt.GlobalColor.black, 2))
            self.scene.addItem(line)

            self.draw_member(child, child_position, generation + 1)

def main():
    app = QApplication(sys.argv)
    window = LoginSignUpWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
