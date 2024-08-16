from mainwindow import *

def login_btn_clicked(current_window, user):
    current_window.destroy()
    set_mainwindow(user)