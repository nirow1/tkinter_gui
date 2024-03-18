import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.geometry('700x500')


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
