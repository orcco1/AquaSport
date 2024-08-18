import tkinter as tk
from controllers.indexController import *

def create_index():
    index = tk.Tk()
    index.title("AquaSport")
    index.geometry("1280x720")

    label_user = tk.Label(index, text="User:")
    entry_user = tk.Entry(index)

    label_password = tk.Label(index, text="Password:")
    entry_password = tk.Entry(index, show="*")

    login_btn = tk.Button(index, text="Login", command=lambda: login_btn_clicked(entry_user.get(), entry_password.get()))

    label_user.pack()
    entry_user.pack()
    label_password.pack()
    entry_password.pack()
    login_btn.pack()

    index.mainloop()

if __name__ == "__main__":
    create_index()