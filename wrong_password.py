import tkinter as tk

def create_warn():
    warn = tk.Tk()
    warn.title("Invalid credentials")
    warn.geometry("640x360")
    label_warn = tk.Label(warn, text="Wrong password or user, try again.")
    label_warn.pack()
    warn.mainloop()

if __name__ == "__main__":
    create_warn()