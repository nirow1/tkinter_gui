import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.window.title("Window with widgets")
        self.window.geometry('800x500')

        label = ttk.Label(master=self.window, text="This is a test")
        label.pack()

        text = tk.Text(master=self.window)
        text.pack()

        entry = ttk.Entry(master=self.window)
        entry.pack()

        button = ttk.Button(master=self.window, text="A button", command=self.button_function)
        button.pack()

    def button_function(self):
        print("button pressed")


if __name__ == '__main__':
    window = MainWindow()
    window.window.mainloop()
