import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.frame = ttk.Frame(self, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
        self.frame2 = ttk.Frame(self, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.geometry('700x500')

        label = ttk.Label(self.frame, text="kabel in frame")
        label.pack()
        self.frame.pack_propagate(False)
        self.frame.pack(side="left")

        label2 = ttk.Label(self.frame2, text="kabel in frame")
        label2.pack()

        self.frame2.pack_propagate(False)
        self.frame2.pack(side="left")


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
