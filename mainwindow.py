import tkinter as tk

def set_mainwindow():
    mainwindow = tk.Tk()
    mainwindow.title("AquaSport")
    mainwindow.geometry("1280x720")

    label = tk.Label(mainwindow, text="Welcome to AquaSport")
    label.pack()

    mainwindow.mainloop()
