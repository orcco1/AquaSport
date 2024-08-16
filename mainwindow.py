import tkinter as tk

def set_mainwindow(user):
    mainwindow = tk.Tk()
    mainwindow.title("AquaSport")
    mainwindow.geometry("1280x720")

    label = tk.Label(mainwindow, text= f"Welcome to AquaSport, {user}")
    label.pack()

    mainwindow.mainloop()
