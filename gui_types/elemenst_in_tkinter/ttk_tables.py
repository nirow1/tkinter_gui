import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.notebook = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.setup_ui()

    def setup_ui(self):
        self.title('Canvas')
        self.notebook.add(self.tab1, text='Tab1')
        self.notebook.add(self.tab2, text='Tab2')
        self.notebook.add(self.tab3, text='Tab2')

        label1 = ttk.Label(self.tab1, text="This is my label for tab number 1")
        button1 = ttk.Button(self.tab1, text="press me")

        label2 = ttk.Label(self.tab2, text="This is my label for tab number 1")
        entry2 = ttk.Entry(self.tab2)

        button3 = ttk.Button(self.tab3, text="press me")
        button32 = ttk.Button(self.tab3, text="you filthy")
        button33 = ttk.Button(self.tab3, text="animal")

        button1.pack()
        label1.pack()
        label2.pack()
        entry2.pack()
        button3.pack()
        button32.pack()
        button33.pack()
        self.notebook.pack()

        self.geometry('700x500')


if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
