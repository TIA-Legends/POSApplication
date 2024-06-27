import tkinter as tk
from views.dashboard import Dashboard

class Authentication:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        # Create widgets for authentication
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

        self.login_button = tk.Button(self.master, text="Login", command=self.show_dashboard)
        self.login_button.pack()

    def show_dashboard(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Add authentication logic here (e.g., check credentials against database)
        # For simplicity, a hardcoded check is used here
        if username == "admin" and password == "admin123":
            self.dashboard_screen = Dashboard()

def main():
    root = tk.Tk()
    auth = Authentication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
