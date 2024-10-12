import tkinter as tk
from tkinter import messagebox

# Hàm để mở trang đăng ký
def open_registration():
    login_window.withdraw()  # Ẩn cửa sổ đăng nhập
    registration_window.deiconify()  # Hiện cửa sổ đăng ký

# Hàm để mở lại trang đăng nhập
def open_login():
    registration_window.withdraw()  # Ẩn cửa sổ đăng ký
    login_window.deiconify()  # Hiện cửa sổ đăng nhập

# Hàm đăng nhập (có thể thêm logic kết nối với backend)
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()
    # Thêm logic kiểm tra đăng nhập tại đây
    messagebox.showinfo("Đăng nhập", f"Chào mừng, {username}!")

# Hàm đăng ký (có thể thêm logic kết nối với backend)
def register():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    confirm_password = reg_confirm_password_entry.get()
    if password != confirm_password:
        messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
    else:
        # Thêm logic lưu thông tin đăng ký tại đây
        messagebox.showinfo("Đăng ký", "Đăng ký thành công!")

# Tạo cửa sổ chính (trang đăng nhập)
login_window = tk.Tk()
login_window.title("Đăng nhập")
login_window.geometry("300x200")

# Các thành phần trong cửa sổ đăng nhập
tk.Label(login_window, text="Tên đăng nhập").pack(pady=5)
login_username_entry = tk.Entry(login_window)
login_username_entry.pack(pady=5)

tk.Label(login_window, text="Mật khẩu").pack(pady=5)
login_password_entry = tk.Entry(login_window, show="*")
login_password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Đăng nhập", command=login)
login_button.pack(pady=10)

register_button = tk.Button(login_window, text="Đăng ký", command=open_registration)
register_button.pack(pady=5)

# Tạo cửa sổ đăng ký (ban đầu bị ẩn)
registration_window = tk.Toplevel()
registration_window.title("Đăng ký")
registration_window.geometry("300x250")
registration_window.withdraw()  # Ẩn cửa sổ này ban đầu

# Các thành phần trong cửa sổ đăng ký
tk.Label(registration_window, text="Tên đăng nhập").pack(pady=5)
reg_username_entry = tk.Entry(registration_window)
reg_username_entry.pack(pady=5)

tk.Label(registration_window, text="Mật khẩu").pack(pady=5)
reg_password_entry = tk.Entry(registration_window, show="*")
reg_password_entry.pack(pady=5)

tk.Label(registration_window, text="Xác nhận mật khẩu").pack(pady=5)
reg_confirm_password_entry = tk.Entry(registration_window, show="*")
reg_confirm_password_entry.pack(pady=5)

register_button = tk.Button(registration_window, text="Đăng ký", command=register)
register_button.pack(pady=10)

login_link = tk.Button(registration_window, text="Quay lại đăng nhập", command=open_login)
login_link.pack(pady=5)

# Khởi chạy chương trình
login_window.mainloop()

