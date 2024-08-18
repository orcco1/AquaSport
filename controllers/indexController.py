from mainwindow import *
from connection import get_data
import wrong_password

def login_btn_clicked(user, password):
    verify_user(user, password)

def verify_user(user, password):
    query = f"SELECT COUNT(*) FROM aquasport_admins WHERE alias = '{user}' AND password = '{password}'"
    result = get_data(query)
    
    if result[0][0] > 0:
        set_mainwindow(user)
        return True
    else:
        print("Usuario o contraseña incorrectos")
        wrong_password.create_warn()
        return False