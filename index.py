import tkinter as tk

window = tk.Tk()

window.title("AquaSport")

window.geometry("1280x720")

label_user = tk.Label(window, text="User:")

entry_user = tk.Entry(window)

label_password = tk.Label(window, text="Password:")

entry_password = tk.Entry(window, show="*")

login_btn = tk.Button(window, text="Login", command=set)

label_user.pack()

entry_user.pack()

label_password.pack()

entry_password.pack()

login_btn.pack()

window.mainloop()
