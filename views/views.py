# views.py

import tkinter as tk

class POSApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Tkinter POS Application")

        # Create widgets
        self.label = tk.Label(self.master, text="Welcome to POS App")
        self.label.pack()

def main():
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
