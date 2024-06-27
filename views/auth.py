# auth.py

import tkinter as tk
from tkinter import messagebox

class Authentication(tk.Frame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.on_login = on_login

        # Create widgets
        self.label = tk.Label(self.master, text="Login to POS")
        self.label.pack()

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()
       
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Add authentication logic here (e.g., check credentials against database)
        # For simplicity, a hardcoded check is used here
        if username == "admin" and password == "admin123":
            self.login_button.config(state=tk.DISABLED)  # Disable login button after successful login
            self.show_welcome_page()
        else:
            self.show_error("Invalid username or password")

    def show_welcome_page(self):
        self.label.config(text="Welcome to TIA Legends")
        self.after(4000, self.on_login)  # Show welcome page for 4 seconds, then call on_login callback

    def show_error(self, message):
        messagebox.showerror("Error", message)
